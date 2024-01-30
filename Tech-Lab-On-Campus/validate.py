#!/usr/bin/env python
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

from producer.solution.producer_sol import mqProducer
from consumer.solution.consumer_sol import mqConsumer
from concurrent.futures import ThreadPoolExecutor

import time

pool_worker = ThreadPoolExecutor(max_workers=1)

def startUpConsumer():
    consumer = mqConsumer("Test Routing Key", "Test Queue Name", "Test Exchange Name")
    consumer.startConsuming()

def runSetup():
    #Setup consumer in thread
    pool_worker.submit(startUpConsumer)
    producer = mqProducer("Test Routing Key", "Test Exchange Name")
    time.sleep(1)
    producer.publishOrder("Setup Validation Success! You're ready to start working. Press CMD/Ctrl + C to Exit")


if __name__ == "__main__":
    runSetup()
