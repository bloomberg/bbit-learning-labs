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

#Class to generate random position data
import random

class positionUpdates():
    def __init__(self) -> None:
        self.__securityTransactionsSize = 10
        self.__currentTransactionPosition = 0
        self.__securityTransactions = self.__generateTransactionList(self.__securityTransactionsSize)

    def __generateTransactionList(self, transactionSize : int) -> None:
        if transactionSize <= 0:
            raise Exception(f"Unable to generate position transactions. Size given is negative. Size:{transactionSize}")

        count = 0
        currentPositionCount = 0
        transactionList = []

        #Internally pre-generate a list of transactions. Limit transactions to always create positive positions
        while count < transactionSize:
            posUpdate = 0
            if count == 0:
                posUpdate = random.randint(1, 1001)
            else:
                posUpdate = random.randint(-400, 1001)
                while currentPositionCount + posUpdate < 0:
                    posUpdate = random.randint(-400, 1001)

            transactionList.append(posUpdate)
            currentPositionCount += posUpdate
            count += 1

        return transactionList

    def getTransactionList(self) -> list:
        return self.__securityTransactions

    def getNextTransaction(self) -> int:
        if self.__currentTransactionPosition >= self.__securityTransactionsSize:
            raise Exception("No more transaction available")

        #Return next transaction and move iterator forward
        rtn = self.__securityTransactions[self.__currentTransactionPosition]
        self.__currentTransactionPosition += 1
        return rtn
    
    def isNextAvailable(self) -> bool:
        return self.__currentTransactionPosition < self.__securityTransactionsSize
