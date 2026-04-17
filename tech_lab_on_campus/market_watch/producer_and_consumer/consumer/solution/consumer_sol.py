import pika
from consumer_interface import mqConsumerInterface

class mqConsumer(mqConsumerInterface):
    def __init__(self, binding_key: str, exchange_name: str, queue_name: str) -> None:
        self.binding_key = binding_key
        self.exchange_name = exchange_name
        self.queue_name = queue_name
        self.setupRMQConnection()

    def setupRMQConnection(self) -> None:
        # Connect to RabbitMQ running in the other container
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host="rabbitmq")
        )
        self.channel = self.connection.channel()

        # Create the queue if it doesn't exist
        self.channel.queue_declare(queue=self.queue_name)

        # Create the exchange if it doesn't exist
        self.channel.exchange_declare(exchange=self.exchange_name, exchange_type="direct")

        # Bind the queue to the exchange with the binding key
        self.channel.queue_bind(
            queue=self.queue_name,
            exchange=self.exchange_name,
            routing_key=self.binding_key
        )

        # Tell RabbitMQ to call on_message_callback when a message arrives
        self.channel.basic_consume(
            queue=self.queue_name,
            on_message_callback=self.on_message_callback,
            auto_ack=False
        )

    def on_message_callback(self, channel, method_frame, header_frame, body) -> None:
        # Acknowledge the message (tell RabbitMQ we got it)
        channel.basic_ack(delivery_tag=method_frame.delivery_tag)
        # Print the message decoded from bytes to string
        print(body.decode("utf-8"))

    def startConsuming(self) -> None:
        print(" [*] Waiting for messages. To exit press CTRL+C")
        self.channel.start_consuming()

    def __del__(self) -> None:
        print("Closing RMQ connection on destruction")
        try:
            self.channel.close()
            self.connection.close()
        except Exception:
            pass
