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

from typing import Set, Iterable
from .accountInterface import accountInterface
from .securityInterface import securityInterface
class portfolioInterface():
    def __init__(self, portfolioName: str, accounts: Set[accountInterface]) -> None:
        pass

    def getAllAccounts(self) -> Iterable[accountInterface]:
        pass

    #Return a collection of accounts that contain have a security or account name in the filter set.
    #If the security filter set is empty only the account filters will be used.
    #If the account filter set is empty on the security filters will be used.
    def getAccounts(self, accountNamesFilter:Set[str], securitiesFilter:Set) -> Iterable[accountInterface]:
        pass 

    def addAccounts(self, accounts: Set[accountInterface]) -> None:
        pass

    def removeAccounts(self, accountNames: Set[str]) -> None:
        pass
