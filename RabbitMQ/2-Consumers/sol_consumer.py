# Copyright 2022 Bloomberg Finance L.P.
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
from concurrent.futures import ThreadPoolExecutor
from interfaces.consumerInterface import consumerInterface
import time
import os

class mqConsumer(consumerInterface):
    def __init__(self, routing_key : str, **kwargs) -> None:
        self.m_routing_key = routing_key
        self.m_pool = ThreadPoolExecutor(max_workers=1)
        self.m_message_handler = kwargs.get("messageHandler")
        self.setupRMQConnection()

    def __del__(self):
        print(f"Closing RMQ connection on destruction")
        self.m_connection.close()

    def setupRMQConnection(self):
        conParams = pika.URLParameters(os.environ['AMQP_URL'])
        
        #Using blocking connection isn't safe across threads. Only use this within a single thread.
        #Our current threadpool has a max of 1 worker.
        self.m_connection = pika.BlockingConnection(parameters=conParams)
        self.m_channel = self.m_connection.channel()
        
        #Create the exchange if not already present
        self.m_exchange = 'RMQ Labs'
        self.m_channel.exchange_declare(self.m_exchange)
        
        #Create the queue if not already present
        self.m_queue_name = 'RMQ Lab Queue'
        self.m_channel.queue_declare(queue=self.m_queue_name)
        self.m_channel.queue_bind(queue=self.m_queue_name, routing_key=self.m_routing_key, exchange=self.m_exchange)
        self.m_channel.basic_consume(self.m_queue_name, self.on_message)
        
    def on_message(self, channel, method_frame, header_frame, body):
        print(f"Incoming Data. Method_Frame:{method_frame}\nHeader_Frame:{header_frame}\nBody:{body}")
        if self.m_message_handler:
            self.m_message_handler(body)

        channel.basic_ack(method_frame.delivery_tag)
        
    def consumeBlock(self):
        try:
            self.m_channel.start_consuming()
        except KeyboardInterrupt:
            self.m_channel.stop_consuming()

    def startConsuming(self):        
        self.m_pool.submit(self.consumeBlock)

    def stopConsuming(self):
        self.m_channel.channel.stop_consuming()
        print("Attempting to join consumer thread")
        self.m_pool.shutdown()

testObj = mqConsumer("Test_Key")
testObj.startConsuming()
time.sleep(300)
testObj.stopConsuming()
