import pika
import os

class mqConsumerInterface:
    def __init__(self, binding_key: str, exchange_name: str, queue_name: str) -> None:
        # Save parameters to class variables
        self.binding_key = binding_key
        self.exchange_name = exchange_name
        self.queue_name = queue_name
        # Call setupRMQConnection
        self.setupRMQConnection()

    def setupRMQConnection(self) -> None:
        # Set-up Connection to RabbitMQ service
        con_params = pika.URLParameters(os.environ["AMQP_URL"])
        self.connection = pika.BlockingConnection(parameters=con_params)
        # Establish Channel
        self.channel = self.connection.channel()
        # Create the exchange if not already present
        if self.exchange_name != None:
            self.exchange = self.channel.exchange_declare(exchange=self.exchange_name)
        # Create Queue if not already present
        if self.queue_name != None:
            self.queue = self.channel.queue_declare(queue=self.queue_name)
       # Bind Binding Key to Queue on the exchange
        self.channel.queue_bind(
            queue= self.queue_name,
            routing_key= self.binding_key,
            exchange=self.exchange_name,
)
        # Set-up Callback function for receiving messages
        pass

    def on_message_callback(
        self, channel, method_frame, header_frame, body
    ) -> None:
        # Acknowledge message
        channel.basic_ack(method_frame.delivery_tag, False)
        #Print message
        print(body)
        # Close channel and connection
        channel.close()
        self.connection.close()

    def startConsuming(self) -> None:
        # Print " [*] Waiting for messages. To exit press CTRL+C"
        print("[*] Waiting for messages. To exit press CTRL+C.")
        # Start consuming messages
        self.channel.start_consuming()
