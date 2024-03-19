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



class mqConsumer(mqConsumerInterface):
    def __init__(self, binding_key: str, exchange_name: str, queue_name: str) -> None:
        # Save parameters to class variables
        self.binding_key = binding_key
        self.exchange_name = exchange_name
        self.queue_name = queue_name
        # Call setupRMQConnection
        self.setupRMQConnection(self)

    def setupRMQConnection(self) -> None:
        # Set-up Connection to RabbitMQ service - test
        conParams = pika.URLParameters(os.environ['AMQP_URL'])
        connection = pika.BlockingConnection(pika.ConnectionParameters(conParams))
        # Establish Channel
        channel = connection.channel()
        # Create Queue if not already present
        channel.queue_declare(queue='Queue')
        # Create the exchange if not already present
        exchange = channel.exchange_declare(exchange='Exchange')
        # Bind Binding Key to Queue on the exchange
        channel.queue_bind(queue='Queue',
                           routing_key='Routing Key',
                           exchange='Exchange')
        # Set-up Callback function for receiving messages
        channel.basic_consume(queue='Exchange', on_message_callback=self.on_message_callback)

    def on_message_callback(self, channel, method_frame, header_frame, body) -> None:
        # Acknowledge message
        channel.basic_ack(method_frame.delivery_tag, False)
        #Print message (The message is contained in the body parameter variable)
        print(f'[x] Received {body}')

    def startConsuming(self) -> None:
        # Print " [*] Waiting for messages. To exit press CTRL+C"
        print('[*] Waiting for messages. To exit press CTRL+C')
        # Start consuming messages
        self.channel.start_consuming()
    
    def __del__(self) -> None:
        # Print "Closing RMQ connection on destruction"
        print('Closing RMQ connections on destruction')
        # Close Channel
        self.channel.close()
        # Close Connection
        self.connection.close()
