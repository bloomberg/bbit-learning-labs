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
import os, json
class mqConsumerInterface:
    def __init__(self, exchange_name: str) -> None:
        # Save parameters to class variables
        self.exchange_name = exchange_name
        
        # Call setupRMQConnection
        self.setupRMQConnection()

    def setupRMQConnection(self) -> None:
        # Set-up Connection to RabbitMQ service
        con_params = pika.URLParameters(os.environ["AMQP_URL"])
        self.connection = pika.BlockingConnection(parameters=con_params)

        # Establish Channel
        self.channel = self.connection.channel()

        # Create the exchange if not already present
        self.exchange = self.channel.exchange_declare(exchange=self.exchange_name)

    def bindQueueToExchange(self, queueName: str, topic: str) -> None:
        # Bind Binding Key to Queue on the exchange
        self.channel.queue_bind(
            queue=queueName,
            # routing_key=topic,
            exchange=self.exchange_name,
        )

    def createQueue(self, queueName: str) -> None:
        # Create Queue if not already present
        self.channel.queue_declare(queue=queueName)

        # Set-up Callback function for receiving messages
        self.channel.basic_consume(
            queueName, on_message_callback=self.on_message_callback, auto_ack=False
        )

    def on_message_callback(self, channel, method_frame, header_frame, body):
        # De-Serialize JSON message object if Stock Object Sent
        message = json.loads(body)

        # Acknowledge And Print Message
        channel.basic_ack(method_frame.delivery_tag, False)
        print(message)

        self.channel.close()
        self.connection.close()

    def startConsuming(self) -> None:
        # Start consuming messages
        print("Started consuming!")
        self.channel.start_consuming()
