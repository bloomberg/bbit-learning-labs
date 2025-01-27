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

import { useState } from "react";
import BuyWindow from "@/components/BuyWindow";
import SellWindow from "@/components/SellWindow";

export default function Share({
  name,
  symbol,
  idx,
  sharePrice,
  oneDChange,
  yourShares,
  avgPrice,
  mktValue,
  yourChange,
  hardCodedUserAmount,
  setHardCodedUserAmount,
  portfolioValue,
  updatePortfolioValue
}) {
  const share = {
    name,
    symbol,
    sharePrice,
    oneDChange,
    yourShares,
    avgPrice,
    mktValue,
    yourChange
  };

  const [revealBuyWindow, setRevealBuyWindow] = useState(false);
  const [revealSellWindow, setRevealSellWindow] = useState(false);

  function getOneDayChangeCSSClass() {
    let color = "";
    if (oneDChange > 0) {
      color = "green";
    } else if (oneDChange < 0) {
      color = "red";
    } else {
      color = "orange";
    }
    return `bg-${color}-200 border-${color}-200 rounded`;
  }

  return (
    <>
      <div className="border-y border-black px-6 py-4">{symbol}</div>
      <div className="border-y border-black dollars px-6 py-4">{sharePrice}</div>
      <div className={`border-y border-black  px-6 py-4`}><span className={`p-1 ${getOneDayChangeCSSClass()}`}>{`${oneDChange > 0 ? "+" : ""}${oneDChange}%`}</span></div>
      <div className="border-y border-black px-6 py-4">{yourShares}</div>
      <div className="border-y border-black dollars px-6 py-4">{avgPrice}</div>
      <div className="border-y border-black dollars px-6 py-4">{mktValue}</div>
      <div className="border-y border-black percentage px-6 py-4">{yourChange}</div>
      <div className="border-y border-black py-4">
        <input className="rounded-full bg-slate-950 text-white text-lg w-1/2 hover:cursor-pointer" type="button" onClick={() => { setRevealBuyWindow(true); setRevealSellWindow(false) }} value="Buy"/>
      </div>
      <div className="border-y border-black py-4">
        <input className="rounded-full bg-slate-950 text-white text-lg w-1/2 hover:cursor-pointer" type="button" onClick={() => { setRevealSellWindow(true); setRevealBuyWindow(false) }} value="Sell"/>
      </div>
      { !revealBuyWindow ? '' : <BuyWindow selectedShare={ share } handleCloseWindow={() => setRevealBuyWindow(false)} idx={idx} hardCodedUserAmount={hardCodedUserAmount} setHardCodedUserAmount={setHardCodedUserAmount} portfolioValue={portfolioValue} updatePortfolioValue={updatePortfolioValue} /> }
      { !revealSellWindow ? '' : <SellWindow selectedShare={ share } handleCloseWindow={() => setRevealSellWindow(false)} idx={idx} hardCodedUserAmount={hardCodedUserAmount} setHardCodedUserAmount={setHardCodedUserAmount} portfolioValue={portfolioValue} updatePortfolioValue={updatePortfolioValue} /> }
    </>
  );
}
