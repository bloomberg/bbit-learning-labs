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

import argparse
import sys

from solution.producer_sol import mqProducer  # pylint: disable=import-error


def main(ticker: str, price: float, sector: str) -> None:
    
    # Implement Logic to Create Routing Key from the ticker and sector variable -  Step 2
    #
    #                       WRITE CODE HERE!!!
    #


    producer = mqProducer(routing_key=routingKey,exchange_name="Tech Lab Topic Exchange")


    # Implement Logic To Create a message variable from the variable EG. "TSLA price is now $500" - Step 3
    #
    #                       WRITE CODE HERE!!!
    #
    
    
    producer.publishOrder(message)

if __name__ == "__main__":

    # Implement Logic to read the ticker, price and sector string from the command line and save them - Step 1
    #
    #                       WRITE CODE HERE!!!
    #

    sys.exit(main(ticker,price,sector))
