/*
  Copyright 2024 Bloomberg Finance L.P.

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
*/

import BuySellWindow from "@/components/BuySellWindow";

export default function BuyWindow({
  selectedShare,
  handleCloseWindow,
  idx,
  hardCodedUserAmount,
  setHardCodedUserAmount,
  portfolioValue,
  updatePortfolioValue
}) {
  async function handleBuySelectedShare({ shareSymbol, shareAmount, shareCount }) {
    const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/buy_share/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        shareSymbol,
        shareAmount: parseFloat(shareAmount),
        shareCount: parseFloat(shareCount),
        hardCodedUserAmount,
        portfolioValue
      })
    });
    const data = await response.json();
    const { newAmount, newPortfolioValue } = data;
    setHardCodedUserAmount(newAmount);
    updatePortfolioValue({ shareAmount, newPortfolioValue })
  }

  return <BuySellWindow selectedShare={selectedShare} actionType="buy" handleActionSelectedShare={handleBuySelectedShare} handleCloseWindow={handleCloseWindow} idx={idx} />;
}
