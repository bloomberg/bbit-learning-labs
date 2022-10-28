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

import pytest
import implementations.positionSolution
from implementations.securitySolution import security
from generators.positionDataGenerator import positionUpdates

def test_positionManagerInits():
    #GIVEN
    EXPECTED_NAME = "DSAQ US Equity"
    EXPECTED_POSITION = 1000
    INPUT_SEC = security(EXPECTED_NAME)

    #WHEN
    testObjA = implementations.positionSolution.position(INPUT_SEC, EXPECTED_POSITION)
    testObjB = implementations.positionSolution.position(EXPECTED_NAME, EXPECTED_POSITION)

    #EXPECT
    assert (testObjA.getSecurity().getName() == EXPECTED_NAME)
    assert (testObjB.getSecurity().getName() == EXPECTED_NAME)
    assert (testObjA.getPosition() == EXPECTED_POSITION)
    assert (testObjB.getPosition() == EXPECTED_POSITION)

def test_positionUpdates():
    #GIVEN
    secData = positionUpdates()
    EXPECTED_POSITION = sum(secData.getTransactionList())
    
    #WHEN
    testObj = implementations.positionSolution.position("TEST", 0)
    for update in secData.getTransactionList():
        testObj.addPosition(update)

    #EXPECT
    assert (testObj.getPosition() == EXPECTED_POSITION)

def test_positionSet():
    #GIVEN
    testObj = implementations.positionSolution.position("TEST", 0)
    EXPECTED_POSITION = 1000
    
    #WHEN
    testObj.setPosition(EXPECTED_POSITION)

    #EXPECT
    assert (testObj.getPosition() == EXPECTED_POSITION)
    
def test_positionUpdateShortBlock():
    #GIVEN
    BASE_POSITION = 100
    UPDATE_POSITION = -101
    testObj = implementations.positionSolution.position("TEST", BASE_POSITION)


    #EXPECT
    with pytest.raises(Exception):
        testObj.addPosition(UPDATE_POSITION)
