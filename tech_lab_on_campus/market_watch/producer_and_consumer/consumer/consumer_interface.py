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


class mqConsumerInterface:
    def __init__(
        self, binding_key: str, exchange_name: str, queue_name: str
    ) -> None:
        # Save parameters to class variables

        # Call setupRMQConnection
        pass

    def setupRMQConnection(self) -> None:
        # Set-up Connection to RabbitMQ service

        # Establish Channel

        # Create Queue if not already present

        # Create the exchange if not already present

        # Bind Binding Key to Queue on the exchange

        # Set-up Callback function for receiving messages
        pass

    def on_message_callback(
        self, channel, method_frame, header_frame, body
    ) -> None:
        # Acknowledge message

        #Print message (The message is contained in the body parameter variable)

        pass

    def startConsuming(self) -> None:
        # Print " [*] Waiting for messages. To exit press CTRL+C"

        # Start consuming messages
        pass
    
    def __del__(self) -> None:
        # Print "Closing RMQ connection on destruction"
        
        # Close Channel

        # Close Connection
        
        pass
