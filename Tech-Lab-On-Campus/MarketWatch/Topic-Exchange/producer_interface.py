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

class mqProducerInterface:
    def __init__(self, exchange_name: str) -> None:
        # Save parameters to class variables

        # Call setupRMQConnection

        pass

    def setupRMQConnection(self) -> None:
        # Set-up Connection to RabbitMQ service

        # Establish Channel

        # Create the topic exchange if not already present

        pass

    def publishOrder(self, message: str) -> None:
        # Create Appropiate Topic String

        # Send serialized message or String

        # Print Confirmation

        # Close channel and connection

        pass
