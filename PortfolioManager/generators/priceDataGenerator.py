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

#Class to generate pseudo random pricing data for a security.
import random

class priceData():
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(priceData, cls).__new__(cls)
            cls._instance.__securityPriceData = {}
            cls._instance.__securityRally = {}
        return cls._instance

    def __identifySecurityType(self, securityName: str) -> bool:
        #Check if the security is an equity. Used internally to limit prices to positive values
        if "eqty" in securityName.casefold() or "equity" in securityName.casefold():
            return True
        
        return False

    def getCurrentPrice(self, securityName: str) -> dict:
        positiveOnly = self.__identifySecurityType(securityName)

        if securityName not in self.__securityPriceData:
            self.__securityPriceData[securityName] = []

        if positiveOnly:
            #Check if we need seed position
            if len(self.__securityPriceData[securityName]) == 0:
                self.__securityPriceData[securityName].append(random.choices(range(0, 10000))[0])
            else:
                #Check if we hit a rally
                if len(self.__securityPriceData[securityName]) > 2 and \
                    self.__securityPriceData[securityName][-1] - self.__securityPriceData[securityName][-2] > 0 and \
                    random.uniform(0, 1) < 0.0005 and \
                    securityName not in self.__securityRally:
                    self.__securityRally[securityName] = 10

                if securityName in self.__securityRally:
                    securityMove = self.__securityPriceData[securityName][-1] * random.uniform(0.05, 0.1)
                    self.__securityRally[securityName] -= 1
                    if self.__securityRally[securityName] <= 0:
                        del self.__securityRally[securityName]
                    self.__securityPriceData[securityName].append(self.__securityPriceData[securityName][-1] + securityMove)
                else:
                    #Generate a move positive or negative. With a percentage move
                    securityMove = self.__securityPriceData[securityName][-1] * random.uniform(0.0001, 0.01)
                    
                #Move security's price based on the generate market value    
                if bool(random.getrandbits(1)):
                    self.__securityPriceData[securityName].append(self.__securityPriceData[securityName][-1] + securityMove)
                else:
                    self.__securityPriceData[securityName].append(self.__securityPriceData[securityName][-1] - securityMove)
        else:
            self.__securityPriceData[securityName].append(random.choices(range(-2000, 10000))[0])

        return self.__securityPriceData[securityName][-1]

    def getPriceDataList(self) -> dict:
        return self.__securityPriceData

    def getSecurityPriceDataList(self, securityName: str) -> list:
        return self.__securityPriceData[securityName]

    def clearPriceHistory(self) -> None:
        self.__securityPriceData = {}
