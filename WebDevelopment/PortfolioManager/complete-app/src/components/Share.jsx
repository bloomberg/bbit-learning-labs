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
