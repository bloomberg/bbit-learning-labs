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

import sol_consumer


def main(tickers: list[str], sectors: list[str], firm: str) -> None:
    consumer = sol_consumer.mqConsumer("Market Watch Exchange")
    consumer.createQueue(firm)

    topics = []

    if tickers:
        [topics.append(f"*.{ticker}.*") for ticker in tickers]
    if sectors:
        [topics.append(f"*.*.{sector}") for sector in sectors]

    for topic in topics:
        consumer.bindQueueToExchange(queueName=firm, topic=topic)

    consumer.startConsuming()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Process Stock Name, Price And Type."
    )

    parser.add_argument(
        "-t",
        "--tickers",
        type=str,
        help="Stock Tickers",
        required=False,
        nargs="+",
    )

    parser.add_argument(
        "-s",
        "--sectors",
        type=str,
        help="Stock Sectors",
        required=False,
        nargs="+",
    )

    parser.add_argument(
        "-f", "--firm", type=str, help="Firm Name", required=True
    )

    args = parser.parse_args()

    if not args.tickers and not args.sectors:
        raise ValueError("Both tickers and sectors cannot be NULL")

    sys.exit(main(args.tickers, args.sectors, args.firm))
