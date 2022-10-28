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

import os
import sys
module_path = os.path.abspath('..')
if module_path not in sys.path:
    sys.path.append(module_path)

from interfaces.accountInterface import accountInterface
from interfaces.securityInterface import securityInterface
from interfaces.positionInterface import positionInterface
from typing import Any, Dict, Set, Iterable
from math import fsum

class account(accountInterface):
    def __init__(self, positions: Set[positionInterface], accountName: str) -> None:
        self.m_accountName = accountName
        self.m_positions = {posItem.getSecurity().getName(): posItem for posItem in positions}

    def getName(self) -> str:
        return self.m_accountName

    def getAllPositions(self) -> Iterable[positionInterface]:
        return list(self.m_positions.values())

    def getPositions(self, securities: Set) -> Dict[Any, positionInterface]:
        returnPostionMap = {}
        
        for securityKey in securities:
            if isinstance(securityKey, securityInterface) and securityKey.getName() in self.m_positions:
                returnPostionMap[securityKey] = self.m_positions[securityKey.getName()]
            elif securityKey in self.m_positions:
                returnPostionMap[securityKey] = self.m_positions[securityKey]

        return returnPostionMap

    def addPositions(self, positions: Set[positionInterface]) -> None:
        for positionItr in positions:
            if positionItr.getSecurity().getName() in self.m_positions:
                self.m_positions[positionItr.getSecurity().getName()].setPosition(positionItr.getPosition())
            else:
                self.m_positions[positionItr.getSecurity().getName()] =  positionItr
    
    def removePositions(self, securities: Set) -> None:
        for securityKey in securities:
            if isinstance(securityKey, securityInterface):
                self.m_positions.pop(securityKey.getName(), None)
            else:
                self.m_positions.pop(securityKey, None)

    def getCurrentMarketValue(self) -> float:
        return fsum([pos.getCurrentMarketValue() for pos in self.m_positions.values()])

    def getCurrentFilteredMarketValue(self, securities: Set) -> float:
        return fsum([pos.getCurrentMarketValue() for pos in self.getPositions(securities).values()])
