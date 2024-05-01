import pika
import os
class mqProducer():
    def __init__(self, routing_key: str, exchange_name: str) -> None:
        # Save parameters to class variables
        self.routing_key = routing_key
        self.exchange_name = exchange_name

        # Call setupRMQConnection
        self.setupRMQConnection()
    def setupRMQConnection(self) -> None:
        # Set-up Connection to RabbitMQ service
        # The AMPQ_URL is a string which tells pika the package the URL of our AMPQ service in this scenario RabbitMQ.
        conParams = pika.URLParameters(os.environ['AMQP_URL'])
        self.connection = pika.BlockingConnection(parameters=conParams)


        # Establish Channel
        self.channel = self.connection.channel()
        # Create the exchange if not already present
        self.channel.exchange_declare(self.exchange_name)

    def publishOrder(self, message: str) -> None:
        # Basic Publish to Exchange
        self.channel.basic_publish(
            exchange = self.exchange_name,
            routing_key = self.routing_key,
            body = message
        )
        # Close Channel
        self.channel.close()
        self.connection.close()
        # Close Connection