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

from interfaces.securityInterface import securityInterface
from interfaces.positionInterface import positionInterface
from implementations.securitySolution import security

class position(positionInterface):
    def __init__(self, securityIn, initialPosition: int) -> None:
        super().__init__(securityIn, initialPosition)
        self.m_PositionValue = initialPosition

        if isinstance(securityIn, securityInterface):
            self.m_security = securityIn
        else:
            self.m_security = security(securityIn)
        
    def getSecurity(self) -> securityInterface:
        return self.m_security
    
    def getPosition(self) -> int:
        return self.m_PositionValue
    
    def setPosition(self, inputValue: int) -> None:
        if inputValue < 0:
            raise Exception("Position update would cause a short position!")
        self.m_PositionValue = inputValue 

    def addPosition(self, inputValue: int) -> None:
        if self.m_PositionValue + inputValue < 0:
            raise Exception("Position update would cause a short position!") 

        self.m_PositionValue += inputValue
