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

import implementations.portfolioSolution
import implementations.securitySolution
import implementations.positionSolution
import implementations.accountSolution
from generators.priceDataGenerator import priceData

def createPortfolioAccounts():
    ACCOUNT_A_POSITIONS = [
        implementations.positionSolution.position("IBM US Equity", 530),
        implementations.positionSolution.position("TSLA US Equity", 1120),
        implementations.positionSolution.position("NVDA US Equity", 7421)
    ]

    ACCOUNT_B_POSITIONS = [
        implementations.positionSolution.position("IBM US Equity", 201),
        implementations.positionSolution.position("MSFT US Equity", 400),
        implementations.positionSolution.position("NVDA US Equity", 300),
        implementations.positionSolution.position("DLTA US Equity", 623)
    ]

    ACCOUNT_A = implementations.accountSolution.account(ACCOUNT_A_POSITIONS, "Account A")
    ACCOUNT_B = implementations.accountSolution.account(ACCOUNT_B_POSITIONS, "Account B")

    ACCOUNTS = {
        "Account A": ACCOUNT_A,
        "Account B": ACCOUNT_B
    }

    return ACCOUNTS

def test_securityValueGather():
    #GIVEN
    SECURITY_NAME = "TSLA US Equity"
    DATA_SOURCE = priceData()
    DATA_SOURCE.clearPriceHistory()

    #WHEN
    testObj = implementations.securitySolution.security(SECURITY_NAME)
    currentPrice = testObj.getCurrentMarketValue()

    #EXPECT
    assert currentPrice == DATA_SOURCE.getSecurityPriceDataList(SECURITY_NAME)[-1]

def test_PositionMarketValue():
    #GIVEN
    EXPECTED_NAME = "IBM US Equity"
    EXPECTED_POSITION_AMOUNT = 1000
    DATA_SOURCE = priceData()
    DATA_SOURCE.clearPriceHistory()

    #WHEN
    testObj = implementations.positionSolution.position(EXPECTED_NAME, EXPECTED_POSITION_AMOUNT)
    MV = testObj.getCurrentMarketValue()
    LASTEST_EXPECTED_MV = EXPECTED_POSITION_AMOUNT * DATA_SOURCE.getSecurityPriceDataList(EXPECTED_NAME)[-1]

    #EXPECT
    assert (LASTEST_EXPECTED_MV == MV)

def test_SecuritySearchAccountMV():
    #GIVEN
    DATA_SOURCE = priceData()
    DATA_SOURCE.clearPriceHistory()
    EXPECTED_ACCOUNT_POSITIONS = [
        implementations.positionSolution.position("IBM US Equity", 530),
        implementations.positionSolution.position("TSLA US Equity", 1120),
        implementations.positionSolution.position("NVDA US Equity", 7421)
    ]
    SEARCH_SECURITIES_LIST =  ["IBM US Equity", implementations.securitySolution.security("NVDA US Equity"), "MSFT US Equity"]
    SEARCH_SECURITIES_TUPLE = [["IBM US Equity", 530], ["NVDA US Equity", 7421]]
    testObj = implementations.accountSolution.account(EXPECTED_ACCOUNT_POSITIONS, "Test Account")

    #WHEN
    MV = testObj.getCurrentFilteredMarketValue(SEARCH_SECURITIES_LIST)
    EXPECTED_MV = 0
    for secTuple in SEARCH_SECURITIES_TUPLE:
        if secTuple[1] != 0:
            EXPECTED_MV +=  secTuple[1] * DATA_SOURCE.getSecurityPriceDataList(secTuple[0])[-1]
    #EXPECT
    assert (EXPECTED_MV == MV)

def test_TotalAccountMV():
    #GIVEN
    EXPECTED_ACCOUNT_POSITIONS = [
        implementations.positionSolution.position("IBM US Equity", 530),
        implementations.positionSolution.position("TSLA US Equity", 1120),
        implementations.positionSolution.position("NVDA US Equity", 7421)
    ]
    DATA_SOURCE = priceData()
    DATA_SOURCE.clearPriceHistory()
    testObj = implementations.accountSolution.account(EXPECTED_ACCOUNT_POSITIONS, "Test Account")

    #WHEN
    MV = testObj.getCurrentMarketValue()
    EXPECTED_MV = 0
    for pos in EXPECTED_ACCOUNT_POSITIONS:
        EXPECTED_MV += pos.getPosition() * DATA_SOURCE.getSecurityPriceDataList(pos.getSecurity().getName())[-1]
    #EXPECT
    assert (EXPECTED_MV == MV)

def test_TotalPortfolioMV():
    PORTFOLIO_NAME = "TestPortfolio"
    ACCOUNTS = createPortfolioAccounts()
    POSITION_MAP_TOTAL = {}

    for acc in ACCOUNTS.values():
        for pos in acc.getAllPositions():
            if pos.getSecurity().getName() in POSITION_MAP_TOTAL:
                POSITION_MAP_TOTAL[pos.getSecurity().getName()].addPosition(pos.getPosition())
            else:
                POSITION_MAP_TOTAL[pos.getSecurity().getName()] = implementations.positionSolution.position(pos.getSecurity(), pos.getPosition())

    DATA_SOURCE = priceData()
    DATA_SOURCE.clearPriceHistory()
    testObj = implementations.portfolioSolution.portfolio(PORTFOLIO_NAME, ACCOUNTS.values())

    MV_TOTAL = testObj.getCurrentMarketValue()
    EXPECTED_MV_TOTAL = 0
    for pos in POSITION_MAP_TOTAL.values():
        EXPECTED_MV_TOTAL += pos.getPosition() * DATA_SOURCE.getSecurityPriceDataList(pos.getSecurity().getName())[-1]
    assert (MV_TOTAL == EXPECTED_MV_TOTAL)

def test_FilteredPortfolioMVs():
    #GIVEN
    PORTFOLIO_NAME = "TestPortfolio"
    ACCOUNTS = createPortfolioAccounts()

    POSITION_MAP_TOTAL_ACC = {}
    POSITION_MAP_TOTAL_SECURITY = {}
    POSITION_MAP_TOTAL_SECURITY_ACC = {}
    SECURITY_FILTER = "IBM US Equity"
    ACC_FILTER = "Account B"
    for acc in ACCOUNTS.values():
        for pos in acc.getAllPositions():
            if pos.getSecurity().getName() == SECURITY_FILTER:
                if pos.getSecurity().getName() in POSITION_MAP_TOTAL_SECURITY:
                    print
                    POSITION_MAP_TOTAL_SECURITY[pos.getSecurity().getName()].addPosition(pos.getPosition())
                else:
                    POSITION_MAP_TOTAL_SECURITY[pos.getSecurity().getName()] = implementations.positionSolution.position(pos.getSecurity().getName(), pos.getPosition())

            if acc.getName() == ACC_FILTER:
                if pos.getSecurity().getName() in POSITION_MAP_TOTAL_ACC:
                    POSITION_MAP_TOTAL_ACC[pos.getSecurity().getName()].addPosition(pos.getPosition())
                else:
                    POSITION_MAP_TOTAL_ACC[pos.getSecurity().getName()] = implementations.positionSolution.position(pos.getSecurity().getName(), pos.getPosition())

                if pos.getSecurity().getName() == SECURITY_FILTER:
                    if pos.getSecurity().getName() in POSITION_MAP_TOTAL_SECURITY_ACC:
                        POSITION_MAP_TOTAL_SECURITY_ACC[pos.getSecurityName()].addPosition(pos.getPosition())
                    else:
                        POSITION_MAP_TOTAL_SECURITY_ACC[pos.getSecurity().getName()] = implementations.positionSolution.position(pos.getSecurity().getName(), pos.getPosition())

    DATA_SOURCE = priceData()
    DATA_SOURCE.clearPriceHistory()
    testObj = implementations.portfolioSolution.portfolio(PORTFOLIO_NAME, ACCOUNTS.values())

    #WHEN
    MV_ACC = testObj.getCurrentFilteredMarketValue([], [ACC_FILTER])
    EXPECTED_MV_ACC = 0
    for pos in POSITION_MAP_TOTAL_ACC.values():
        EXPECTED_MV_ACC += pos.getPosition() * DATA_SOURCE.getSecurityPriceDataList(pos.getSecurity().getName())[-1]
    DATA_SOURCE = priceData()
    DATA_SOURCE.clearPriceHistory()

    MV_SECURITY = testObj.getCurrentFilteredMarketValue([SECURITY_FILTER], [])
    EXPECTED_MV_SECURITY = 0
    for pos in POSITION_MAP_TOTAL_SECURITY.values():
        EXPECTED_MV_SECURITY += pos.getPosition() * DATA_SOURCE.getSecurityPriceDataList(pos.getSecurity().getName())[-1]
    DATA_SOURCE = priceData()
    DATA_SOURCE.clearPriceHistory()

    MV_ACC_SECURITY = testObj.getCurrentFilteredMarketValue([SECURITY_FILTER], [ACC_FILTER])
    EXPECTED_MV_ACC_SECURITY = 0
    for pos in POSITION_MAP_TOTAL_SECURITY_ACC.values():
        EXPECTED_MV_ACC_SECURITY += pos.getPosition() * DATA_SOURCE.getSecurityPriceDataList(pos.getSecurity().getName())[-1]
    DATA_SOURCE = priceData()
    DATA_SOURCE.clearPriceHistory()

    #EXPECT
    assert (MV_ACC == EXPECTED_MV_ACC) 
    assert (MV_ACC_SECURITY == EXPECTED_MV_ACC_SECURITY) 
    assert (MV_SECURITY == EXPECTED_MV_SECURITY) 
