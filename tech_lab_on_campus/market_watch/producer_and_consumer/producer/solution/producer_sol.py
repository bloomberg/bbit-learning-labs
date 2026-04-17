

import os

import pika  # pylint: disable=import-error
from producer_interface import mqProducerInterface


class mqProducer(mqProducerInterface):
    def __init__(self, routing_key: str, exchange_name: str) -> None:
        # Save parameters to class variables
        self.m_routing_key = routing_key
        self.m_exchange_name = exchange_name

        # Call setupRMQConnection
        self.setupRMQConnection()

    def setupRMQConnection(self) -> None:
        # Set-up Connection to RabbitMQ service
        con_params = pika.URLParameters(os.environ["AMQP_URL"])
        self.m_connection = pika.BlockingConnection(parameters=con_params)

        # Establish Channel
        self.m_channel = self.m_connection.channel()

        # Create the exchange if not already present
        self.m_channel.exchange_declare(
            self.m_exchange_name, exchange_type="topic"
        )

    def publishOrder(self, message: str) -> None:
        # Publish a simple UTF-8 string message from the parameter
        self.m_channel.basic_publish(
            exchange=self.m_exchange_name,
            routing_key=self.m_routing_key,
            body=message.encode("utf-8"),
        )

        # Close Channel
        self.m_channel.close()

        # Close Connection
        self.m_connection.close()
