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
from interfaces.producerInterface import producerInterface
import time
import threading
from typing import Any
import os

class mqProducer(producerInterface):
    def __init__(self, routing_key : str, pub_delay : int, message_producer : Any) -> None:
        self.m_routing_key = routing_key
        self.m_pub_delay = pub_delay
        self.m_pub_producer = message_producer
        self.m_run = threading.Event()
        self.m_pool = ThreadPoolExecutor(max_workers=1)
        self.setupRMQConnection()

    def __del__(self):
        print(f"Closing RMQ connection on destruction")
        self.m_connection.close()


    def setupRMQConnection(self):
        conParams = pika.URLParameters(os.environ['AMQP_URL'])
        
        #Using blocking connection isn't safe across threads. Only use this within a single thread.
        #Our current threadpool has a max of 1 work.
        self.m_connection = pika.BlockingConnection(parameters=conParams)
        self.m_channel = self.m_connection.channel()
        
        #Create the exchange if not already present
        self.m_exchange = 'RMQ Labs'
        self.m_channel.exchange_declare(self.m_exchange)
        
    def startPublishing(self):
        if self.m_run.is_set():
            print("Publishing thread started. No-op")
            return

        #Turn on our threading flag & start a thread which runs our publishing loop
        self.m_run.set()
        self.m_pool.submit(self.pubLoop)

    def stopPublishing(self):
        self.m_run.clear()
        print("Attempting to join pub thread")
        self.m_pool.shutdown()

    def pubLoop(self):
        while self.m_run.is_set():
            if self.m_pub_producer:
                data = self.m_pub_producer()
            else:
                data = f"The current time is {time.time()} in epoch time. Routing key is {self.m_routing_key}"
            
            print(f"Submitting data message {data}")
            self.m_channel.basic_publish(self.m_exchange,
                self.m_routing_key,
                data,
                pika.BasicProperties(content_type='text/plain',
                    delivery_mode=pika.DeliveryMode.Transient))
            time.sleep(self.m_pub_delay)

testObj = mqProducer("Test_Key", 1, None)
testObj.startPublishing()
time.sleep(40)
testObj.stopPublishing()
