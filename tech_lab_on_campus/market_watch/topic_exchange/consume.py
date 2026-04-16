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

from solution.consumer_sol import mqConsumer  # pylint: disable=import-error

def main(sector: str, queueName: str) -> None:
    
    bindingKey = f"stock.*.{sector}"
    
    consumer = mqConsumer(binding_key=bindingKey,exchange_name="Tech Lab Topic Exchange",queue_name=queueName)    
    consumer.startConsuming()
    


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Consume stock price updates by sector")
    parser.add_argument("--sector", required=True, help="Industry sector to subscribe to (e.g. tech, healthcare)")
    parser.add_argument("--queue", required=True, help="Queue name (must be unique per consumer)")
    args = parser.parse_args()
    sector = args.sector
    queue = args.queue

    sys.exit(main(sector,queue))
