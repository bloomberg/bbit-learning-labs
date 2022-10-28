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

from implementations.accountSolution import account
from implementations.positionSolution import position
import implementations.portfolioSolution
import pytest

def test_GetAllAccounts():
    #GIVEN
    PORTFOLIO_NAME = "TestPortfolio"
    ACCOUNT_A_POSITIONS = [
        position("MSFT US Equity", 1000),
        position("TSLA US Equity", 2000),
    ]
    ACCOUNT_B_POSITIONS = [
        position("APPL US Equity", 500),
        position("RIVN US Equity", 1000),
    ]
    ACCOUNT_A = account(ACCOUNT_A_POSITIONS, "Account A")
    ACCOUNT_B = account(ACCOUNT_B_POSITIONS, "Account B")

    ACCOUNTS = set([ACCOUNT_A, ACCOUNT_B])
    EXPECTED_ACCOUNTS = {acc.getName():True for acc in ACCOUNTS}

    #WHEN
    p = implementations.portfolioSolution.portfolio(PORTFOLIO_NAME, ACCOUNTS)

    #EXPECT
    ALL_ACCS = p.getAllAccounts()
    
    for acc in ALL_ACCS:
        assert acc.getName() in EXPECTED_ACCOUNTS
        EXPECTED_ACCOUNTS[acc.getName()] = False
    
    assert True not in EXPECTED_ACCOUNTS.values()

@pytest.mark.parametrize("inputAccount, inputSecurity, expectedMap", (
    ([], [], {"Account A": True, "Account B": True, "Account C": True}),
    (["Account A", "Account B", "Account DNE"], [], {"Account A": True, "Account B": True}),
    ([], ["IBM US Equity", "FOOD US Equity"], {"Account A": True, "Account B": True, "Account C": True}),
    (["Account B", "Account C"], ["IBM US Equity"], {"Account B": True})
))
def test_GetSubsetAccounts(inputAccount, inputSecurity, expectedMap):
    #GIVEN
    PORTFOLIO_NAME = "TestPortfolio"
    ACCOUNT_A_POSITIONS = [
        position("MSFT US Equity", 1000),
        position("TSLA US Equity", 2000),
        position("IBM US Equity", 3000)
    ]
    ACCOUNT_B_POSITIONS = [
        position("APPL US Equity", 500),
        position("RIVN US Equity", 1000),
        position("IBM US Equity", 1234)
    ]
    ACCOUNT_C_POSITIONS = [
        position("SWS US Equity", 241),
        position("CORE US Equity", 4213),
        position("FOOD US Equity", 1234)
    ]
    ACCOUNT_A = account(ACCOUNT_A_POSITIONS, "Account A")
    ACCOUNT_B = account(ACCOUNT_B_POSITIONS, "Account B")
    ACCOUNT_C = account(ACCOUNT_C_POSITIONS, "Account C")

    ACCOUNTS = set([ACCOUNT_A, ACCOUNT_B, ACCOUNT_C])

    #WHEN
    p = implementations.portfolioSolution.portfolio(PORTFOLIO_NAME, ACCOUNTS)

    #EXPECT
    FILTERED_ACCOUNTS = p.getAccounts(inputAccount, inputSecurity)
    
    for acc in FILTERED_ACCOUNTS:
        assert acc.getName() in expectedMap
        expectedMap[acc.getName()] = False
    
    assert True not in expectedMap.values()

def test_AddAccountsNoOverwrite():
    #GIVEN
    PORTFOLIO_NAME = "TestPortfolio"
    ACCOUNT_A_POSITIONS = [
        position("MSFT US Equity", 1000),
        position("TSLA US Equity", 2000),
    ]
    ACCOUNT_B_POSITIONS = [
        position("APPL US Equity", 500),
        position("RIVN US Equity", 1000),
    ]
    ACCOUNT_A = account(ACCOUNT_A_POSITIONS, "Account A")
    ACCOUNT_B = account(ACCOUNT_B_POSITIONS, "Account B")

    ACCOUNTS = set([ACCOUNT_A, ACCOUNT_B])
    EXPECTED_ACCOUNTS = {acc.getName():True for acc in ACCOUNTS}

    #WHEN
    p = implementations.portfolioSolution.portfolio(PORTFOLIO_NAME, [])
    p.addAccounts(ACCOUNTS)

    #EXPECT
    ALL_ACCS = p.getAllAccounts()
    
    for acc in ALL_ACCS:
        assert acc.getName() in EXPECTED_ACCOUNTS
        EXPECTED_ACCOUNTS[acc.getName()] = False
    
    assert True not in EXPECTED_ACCOUNTS.values()

def test_AddAccountOverwrite():
    #GIVEN
    PORTFOLIO_NAME = "TestPortfolio"
    ACCOUNT_A_POSITIONS = [
        position("MSFT US Equity", 1000),
        position("TSLA US Equity", 2000),
    ]
    ACCOUNT_B_POSITIONS = [
        position("APPL US Equity", 500),
        position("RIVN US Equity", 1000),
    ]
    ACCOUNT_A = account(ACCOUNT_A_POSITIONS, "Account A")
    ACCOUNT_B = account(ACCOUNT_B_POSITIONS, "Account B")
    ACCOUNTS = set([ACCOUNT_A, ACCOUNT_B])

    #WHEN
    p = implementations.portfolioSolution.portfolio(PORTFOLIO_NAME, ACCOUNTS)
    ACCOUNT_B_POSITIONS_NEW = [
        position("PELO US Equity", 500),
        position("IBM US Equity", 1000),
    ]
    ACCOUNT_B_NEW = account(ACCOUNT_B_POSITIONS_NEW, "Account B")
    EXPECTED_ACCOUNTS = {
        "Account A": ACCOUNT_A_POSITIONS,
        "Account B": ACCOUNT_B_POSITIONS_NEW
    }
    p.addAccounts([ACCOUNT_B_NEW])

    #EXPECT
    ALL_ACCS = p.getAllAccounts()
    
    for acc in ALL_ACCS:
        assert acc.getName() in EXPECTED_ACCOUNTS
        POS_EXPECTED = {x.getSecurity().getName(): x.getPosition() for x in EXPECTED_ACCOUNTS[acc.getName()]}
        RETURN_POS = acc.getAllPositions()

        for pos in RETURN_POS:
            assert pos.getSecurity().getName() in POS_EXPECTED
            assert POS_EXPECTED[pos.getSecurity().getName()] == pos.getPosition()

            #Remove the validate position from out expected map
            del POS_EXPECTED[pos.getSecurity().getName()]

        assert len(POS_EXPECTED) == 0

def test_RemoveAccounts():
    #GIVEN
    PORTFOLIO_NAME = "TestPortfolio"
    ACCOUNT_A_POSITIONS = [
        position("MSFT US Equity", 1000),
        position("TSLA US Equity", 2000),
    ]
    ACCOUNT_B_POSITIONS = [
        position("APPL US Equity", 500),
        position("RIVN US Equity", 1000),
    ]
    ACCOUNT_A = account(ACCOUNT_A_POSITIONS, "Account A")
    ACCOUNT_B = account(ACCOUNT_B_POSITIONS, "Account B")

    ACCOUNTS = set([ACCOUNT_A, ACCOUNT_B])
    EXPECTED_ACCOUNTS = {"Account A": True}

    #WHEN
    p = implementations.portfolioSolution.portfolio(PORTFOLIO_NAME, ACCOUNTS)
    p.removeAccounts(["Account B", "Account DNE"])

    #EXPECT
    ALL_ACCS = p.getAllAccounts()
    
    for acc in ALL_ACCS:
        assert acc.getName() in EXPECTED_ACCOUNTS
        EXPECTED_ACCOUNTS[acc.getName()] = False
    
    assert True not in EXPECTED_ACCOUNTS.values()
