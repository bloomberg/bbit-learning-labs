# Copyright 2024 Bloomberg Finance L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

import pika  # pylint: disable=import-error
from producer_interface import mqProducerInterface
from stock import Stock


class mqProducer(mqProducerInterface):
    def __init__(self, exchange_name: str) -> None:
        # Save parameters to class variables
        self.m_exchange_name = exchange_name

        # Call setupRMQConnection
        self.setupRMQConnection()

    def setupRMQConnection(self) -> None:
        # Set-up Connection to RabbitMQ service
        con_params = pika.URLParameters(os.environ["AMQP_URL"])
        self.m_connection = pika.BlockingConnection(parameters=con_params)

        # Establish Channel
        self.m_channel = self.m_connection.channel()

        # Create the topic exchange if not already present
        self.m_channel.exchange_declare(
            self.m_exchange_name, exchange_type="topic"
        )

    def publishOrder(self, sector: str, stock: Stock) -> None:
        # Create Appropiate Topic String
        topic = f"Stock.{stock.get_name()}.{sector}"
        topic.strip()

        # Send serialized message
        self.m_channel.basic_publish(
            exchange=self.m_exchange_name,
            routing_key=topic,
            body=stock.serialize(),
        )

        # Print Confirmation
        print(f" [x] Sent Order: {topic}")

        # Close channel and connection
        self.m_channel.close()
        self.m_connection.close()
