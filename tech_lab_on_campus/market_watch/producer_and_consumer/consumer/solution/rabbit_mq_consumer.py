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

import pika
import os

from consumer_interface import mqConsumerInterface

class RabbitMQConsumer(mqConsumerInterface):
    def __init__(
        self, binding_key: str, exchange_name: str, queue_name: str
    ) -> None:
        # Save parameters to class variables

        self.binding_key = binding_key
        self.exchange_name = exchange_name
        self.queue_name = queue_name
        self.channel    = None
        self.connection = None

        # Call setupRMQConnection
        self.setupRMQConnection()

        pass

    def setupRMQConnection(self) -> None:

        # Set-up Connection to RabbitMQ service
        con_params = pika.URLParameters(os.environ["AMQP_URL"])
        self.connection = pika.BlockingConnection(con_params)

        # Establish Channel
        self.channel = self.connection.channel()

        # Create Queue if not already present
        self.channel.queue_declare(queue=self.queue_name)

        # Create the exchange if not already present
        self.channel.exchange_declare(
            exchange=self.exchange_name,
            exchange_type="direct",
            durable=True
        )
    
        # Bind Binding Key to Queue on the exchange
        self.channel.queue_bind(queue=self.queue_name,exchange=self.exchange_name,routing_key=self.binding_key)

        # Set-up Callback function for receiving messages
        self.channel.basic_consume(queue=self.queue_name, on_message_callback=self.on_message_callback)

    def on_message_callback(
        self, channel, method_frame, header_frame, body
    ) -> None:
        # Acknowledge message
        channel.basic_ack(method_frame.delivery_tag)

        #Print message (The message is contained in the body parameter variable)
        print(f"Received: {body}")

    def startConsuming(self):
        print("Started message consumption: waiting for message...")

        self.channel.start_consuming()

    def __del__(self) -> None:

        # Print "Closing RMQ connection on destruction"
        print("Closing RMQ connection on destruction")

        # Close Channel
        if self.channel: 
            self.channel.close()
            self.channel = None

        # Close Connection
        if self.connection:
            self.connection.close()
            self.connection = None
