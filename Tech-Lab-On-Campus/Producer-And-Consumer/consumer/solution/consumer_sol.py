from consumer_interface import mqConsumerInterface
import pika
import os

class mqConsumer(mqConsumerInterface):
    def __init__(
        self, binding_key: str, exchange_name: str, queue_name: str
        ) -> None:
        self.binding_key = binding_key
        self.exchange_name = exchange_name 
        self.queue_name = queue_name
        self.setupRMQConnection()

    def setupRMQConnection(self):
        # Set-up Connection to RabbitMQ service
        self.con_params = pika.URLParameters(os.environ["AMQP_URL"])
        self.connection = pika.BlockingConnection(parameters=self.con_params)

        # Establish Channel
        self.channel = self.connection.channel()

        # Create Queue if not already present
        self.channel.queue_declare(queue="Tech Lab Queue")

        # Create the exchange if not already present
        self.exchange = self.channel.exchange_declare(exchange="Tech Lab Exchange")

        # Bind Binding Key to Queue on the exchange
        self.channel.queue_bind(
            queue= "Tech Lab Queue",
            routing_key= "Routing Key",
            exchange="Tech Lab Exchange",
        )

        # Set-up Callback function for receiving messages
        self.channel.basic_consume(
            "Tech Lab Queue", self.on_message_callback , auto_ack=False
        )

    def on_message_callback(
        self, channel, method_frame, header_frame, body
        ) -> None:
        # Acknowledge message
        channel.basic_ack(method_frame.delivery_tag, False)

        #Print message (The message is contained in the body parameter variable)
        print(body)


    def startConsuming(self) -> None:
        # Print " [*] Waiting for messages. To exit press CTRL+C"
        print("[*] Waiting for messages. To exit press CTRL+C")

        # Start consuming messages
        self.channel.start_consuming()

    def __del__(self) -> None:
        # Print "Closing RMQ connection on destruction"
        print("Closing RMQ connection on destruction")

        # Close Channel
        self.channel.close()

        # Close Connection
        self.connection.close()






