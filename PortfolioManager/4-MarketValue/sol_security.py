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
from generators.priceDataGenerator import priceData

class security(securityInterface):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.m_name = name
        self.m_priceData = priceData()
        
    def getName(self) -> str:
        return self.m_name

    def getCurrentMarketValue(self) -> float:
        return self.m_priceData.getCurrentPrice(self.m_name)
