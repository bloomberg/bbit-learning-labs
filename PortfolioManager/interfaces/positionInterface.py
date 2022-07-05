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

#Position Class Interface. 
from .securityInterface import securityInterface
class positionInterface():
    def __init__(self, security, initialPosition: int) -> None:
        pass
    
    def getSecurity(self) -> securityInterface:
        pass

    def getPosition(self) -> int:
        pass
    
    def setPosition(self, inputValue: int) -> None:
        pass
    
    #Add an integer amount to the current position.
    def addPosition(self, inputValue: int) -> None:
        pass
