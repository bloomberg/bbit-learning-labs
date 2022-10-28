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

#Portfolio Class
from typing import Set, Iterable
from interfaces.portfolioInterface import portfolioInterface
from interfaces.accountInterface import accountInterface

class portfolio(portfolioInterface):
    def __init__(self, portfolioName: str, accounts: Set[accountInterface]) -> None:
        super().__init__(portfolioName, accounts)
        self.m_name = portfolioName
        self.m_accounts =  {accItem.getName(): accItem for accItem in accounts}

    def getAllAccounts(self) -> Iterable[accountInterface]:
        return list(self.m_accounts.values())

    def getAccounts(self, accountNamesFilter:Set[str], securitiesFilter:Set) -> Iterable[accountInterface]:
        if (len(accountNamesFilter) == 0 and len(securitiesFilter) == 0):
            return self.getAllAccounts()
        
        if len(accountNamesFilter) != 0:
            filteredAcc = set()

            for acc in accountNamesFilter:
                if acc in self.m_accounts:
                    filteredAcc.add(self.m_accounts[acc])
        else:
            filteredAcc = set(self.m_accounts.values())

        finalSet = set()
        if len(securitiesFilter) != 0:
            for acc in filteredAcc:
                if len(acc.getPositions(securitiesFilter)) != 0:
                    finalSet.add(acc)
        else:
            finalSet = filteredAcc

        return finalSet   

    def addAccounts(self, accounts: Set[accountInterface]) -> None:
        for accounts in accounts:
            self.m_accounts[accounts.getName()] = accounts

    def removeAccounts(self, accountNames: Set[str]) -> None:
        for accName in accountNames:
            self.m_accounts.pop(accName, None)

