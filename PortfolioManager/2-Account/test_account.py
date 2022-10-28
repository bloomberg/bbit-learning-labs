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

from implementations.securitySolution import security
from implementations.positionSolution import position
import implementations.accountSolution

def test_getAccountName():
    #GIVEN
    EXPECTED_NAME = "MY TEST ACCOUNT"
    EXPECTED_POSITIONS = set()

    #WHEN 
    testObj = implementations.accountSolution.account(EXPECTED_POSITIONS, EXPECTED_NAME)

    #EXPECT 
    assert(testObj.getName() == EXPECTED_NAME)

def test_getAllPositions():
    #GIVEN
    EXPECTED_NAME = "MY TEST ACCOUNT"
    EXPECTED_POSITIONS = set()
    EXPECTED_POSITIONS.add(position("TEST_SEC_A", 1000))
    EXPECTED_POSITIONS.add(position("TEST_SEC_B", 2000))

    #WHEN 
    testObj = implementations.accountSolution.account(EXPECTED_POSITIONS, EXPECTED_NAME)
    returnPosItr = testObj.getAllPositions()

    #EXPECT
    assert(len(returnPosItr) == len(EXPECTED_POSITIONS))

    for item in list(returnPosItr):
        assert(item in EXPECTED_POSITIONS)
        EXPECTED_POSITIONS.remove(item)
        returnPosItr.remove(item)

    assert(len(returnPosItr) == 0)
    assert(len(EXPECTED_POSITIONS) == 0)

def test_getPositions():
    #GIVEN
    EXPECTED_NAME = "MY TEST ACCOUNT"
    EXPECTED_POSITIONS = set()
    EXPECTED_POSITIONS.add(position("TEST_SEC_A", 1000))
    EXPECTED_POSITIONS.add(position("TEST_SEC_B", 2000))
    KEY_LIST = [security("TEST_SEC_A"), "TEST_SEC_B", "TEST_NOT_FOUND_STR", security("TEST_NOT_FOUND_POS")]
    EXPECTED_MAP = {
        KEY_LIST[0] : position("TEST_SEC_A", 1000), 
        KEY_LIST[1] : position("TEST_SEC_B", 2000),
    }

    #WHEN 
    testObj = implementations.accountSolution.account(EXPECTED_POSITIONS, EXPECTED_NAME)
    returnPosItr = testObj.getPositions(KEY_LIST)

    #EXPECT
    assert(len(returnPosItr) == len(KEY_LIST) - 2)
    print(returnPosItr)
    for item in KEY_LIST:
        if isinstance(item, security) and "NOT_FOUND" in item.getName():
            assert item not in returnPosItr
        elif isinstance(item, str) and "NOT_FOUND" in item:
            assert item not in returnPosItr
        else:
            assert(item in returnPosItr)
            assert(returnPosItr[item].getSecurity().getName() == EXPECTED_MAP[item].getSecurity().getName())
            assert(returnPosItr[item].getPosition() == EXPECTED_MAP[item].getPosition())

def test_addPositions():
    EXPECTED_NAME = "MY TEST ACCOUNT"
    START_POSITIONS = set([position("TEST_SEC_A", 1000), position("TEST_SEC_B", 2000)])
    UPDATE_POSITIONS = set([position("TEST_SEC_B", 3000), position("TEST_SEC_C", 1500)])
    EXPECTED_POSITIONS = {
        "TEST_SEC_A" : 1000,
        "TEST_SEC_B" : 3000,
        "TEST_SEC_C" : 1500
    }

    #WHEN 
    testObj = implementations.accountSolution.account(START_POSITIONS, EXPECTED_NAME)
    testObj.addPositions(UPDATE_POSITIONS)
    returnPosItr = testObj.getAllPositions()

    #EXPECT
    assert(len(returnPosItr) == len(EXPECTED_POSITIONS))

    for item in list(returnPosItr):
        assert(item.getSecurity().getName() in EXPECTED_POSITIONS)
        assert(item.getPosition() ==  EXPECTED_POSITIONS[item.getSecurity().getName()])
        del EXPECTED_POSITIONS[item.getSecurity().getName()]
        returnPosItr.remove(item)

    assert(len(returnPosItr) == 0)
    assert(len(EXPECTED_POSITIONS) == 0)

def test_removePositions():
    EXPECTED_NAME = "MY TEST ACCOUNT"
    START_POSITIONS = set([position("TEST_SEC_A", 1000), position("TEST_SEC_B", 2000), position("TEST_SEC_C", 1500), position("TEST_SEC_D", 3500)])
    REMOVE_POSITIONS = set([security("TEST_SEC_B"), security("TEST_SEC_C")])
    EXPECTED_POSITIONS = {
        "TEST_SEC_A" : 1000,
        "TEST_SEC_D" : 3500
    }

    #WHEN 
    testObj = implementations.accountSolution.account(START_POSITIONS, EXPECTED_NAME)
    testObj.removePositions(REMOVE_POSITIONS)
    returnPosItr = testObj.getAllPositions()

    #EXPECT
    assert(len(returnPosItr) == len(EXPECTED_POSITIONS))

    for item in list(returnPosItr):
        assert(item.getSecurity().getName() in EXPECTED_POSITIONS)
        assert(item.getPosition() ==  EXPECTED_POSITIONS[item.getSecurity().getName()])
        del EXPECTED_POSITIONS[item.getSecurity().getName()]
        returnPosItr.remove(item)

    assert(len(returnPosItr) == 0)
    assert(len(EXPECTED_POSITIONS) == 0)
