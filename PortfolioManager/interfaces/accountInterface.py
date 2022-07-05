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

from .positionInterface import positionInterface
from typing import Any, Dict, Set, Iterable
class accountInterface():
    def __init__(self, positions: Set[positionInterface], accountName: str) -> None:
        pass

    #Return the account's name
    def getName(self) -> str:
        pass

    #Return all positions currently within the account
    def getAllPositions(self) -> Iterable[positionInterface]:
        pass

    #Return all positions that contain a security in a given input set
    def getPositions(self, securities: Set) -> Dict[Any, positionInterface]:
        pass

    #Add positions to the account
    def addPositions(self, positions: Set[positionInterface]) -> None:
        pass
    
    #Remove a number of positions from this account if they represent a security in a given input set
    def removePositions(self, securities: Set) -> None:
        pass
