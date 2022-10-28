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

from bqplot import pyplot as plt
import os
import sys
module_path = os.path.abspath('..')
if module_path not in sys.path:
    sys.path.append(module_path)
from implementations.securitySolution import security

def createSecurityMV(securityName, dataPointSize):
    size = dataPointSize
    securityObj = security(securityName)
    MV = {}
    count = 0
    while count < size:
        MV[count] = securityObj.getCurrentMarketValue()
        count += 1

    x_data = list(MV.keys())
    y_data = list(MV.values())

    plt.figure(title=securityObj.getName(), animation_duration=1000)
    plt.plot(x_data, y_data)
    plt.show()
    return plt
    
plt = createSecurityMV("IBM US Equity", 1000)
