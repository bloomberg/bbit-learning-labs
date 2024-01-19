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

import sol_producer


def main(ticker: str, price: float, sector: str) -> None:
    marketWatch = sol_producer.mqProducer("Market Watch Exchange")

    stock = sol_producer.Stock(ticker, price)

    marketWatch.publishOrder(sector=sector, stock=stock)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Process Stock Name, Price And Type."
    )

    parser.add_argument(
        "-t", "--ticker", type=str, help="Stock Ticker", required=True
    )
    parser.add_argument(
        "-p", "--price", type=float, help="Stock Price", required=True
    )
    parser.add_argument(
        "-s", "--sector", type=str, help="Stock Sector", required=True
    )

    args = parser.parse_args()

    sys.exit(main(args.ticker, args.price, args.sector))
