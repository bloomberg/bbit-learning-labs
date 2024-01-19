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

import json
import os

import pika
from consumer_interface import mqConsumerInterface


class mqConsumer(mqConsumerInterface):
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

        # Create the exchange if not already present
        self.m_channel.exchange_declare(
            self.m_exchange_name, exchange_type="topic"
        )

    def bindQueueToExchange(self, queueName: str, topic: str) -> None:
        # Bind Binding Key to Queue on the exchange
        self.m_channel.queue_bind(
            queue=queueName, routing_key=topic, exchange=self.m_exchange_name
        )

    def createQueue(self, queueName: str) -> None:
        # Create Queue if not already present
        self.m_channel.queue_declare(queue=queueName)

        # Set-up Callback function for receiving messages
        self.m_channel.basic_consume(
            queueName, self.on_message_callback, auto_ack=True
        )

    def on_message_callback(
        self, channel, method_frame, header_frame, body
    ) -> None:
        # De-Serialize JSON message object
        message = json.loads(body)

        # Acknowledge And Print Message
        print(f"{message['name']} current price is ${message['price']}")

    def startConsuming(self) -> None:
        # Start consuming messages
        print(" [*] Waiting for messages. To exit press CTRL+C")
        self.m_channel.start_consuming()

    def __del__(self) -> None:
        print(f"Closing RMQ connection on destruction")
        self.m_channel.close()
        self.m_connection.close()
