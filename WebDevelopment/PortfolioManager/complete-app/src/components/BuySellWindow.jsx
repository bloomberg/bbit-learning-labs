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
import CloseButton from "@/components/CloseButton";

export default function BuySellWindow({ selectedShare, actionType, handleActionSelectedShare, handleCloseWindow, idx }) {
  const [amountSharesFieldValue, setAmountSharesFieldValue] = useState('');
  const [sharesFieldValue, setSharesFieldValue] = useState('');
  const [showNotEnoughSharesMsg, setShowNotEnoughSharesMsg] = useState(false);

  function updateAmountSharesField(amount, sharePrice) {
    setAmountSharesFieldValue(amount);

    if (!amount) {
      setSharesFieldValue('');
    } else {
      const shares = parseFloat((amount / sharePrice).toFixed(3));
      setSharesFieldValue(shares);
      renderNotEnoughSharesMsg(shares);
    }
  }

  function updateSharesField(shares, sharePrice) {
    setSharesFieldValue(shares);

    if (!shares) {
      setAmountSharesFieldValue('');
    } else {
      const amountShares = parseFloat((shares * sharePrice)).toFixed(3);
      setAmountSharesFieldValue(amountShares);
      renderNotEnoughSharesMsg(shares);
    }
  }

  function renderNotEnoughSharesMsg(shareCount) {
    if (actionType === "sell" && shareCount > selectedShare["yourShares"]) {
        setShowNotEnoughSharesMsg(true);
    } else {
        setShowNotEnoughSharesMsg(false);
    }
  }

  function handleClickOnActionButton() {
    handleActionSelectedShare({
      shareSymbol: selectedShare["symbol"],
      shareAmount: amountSharesFieldValue,
      shareCount: sharesFieldValue
    });
  }

  return (
    <div className="p-5 col-span-9">
      <div className="relative">
        <CloseButton onClickHandler={handleCloseWindow} />
      </div>
      <p className="font-bold">{actionType === "buy" ? "Buy" : "Sell"} {`${selectedShare["symbol"]}:${selectedShare["name"]}`}</p>
      <div className="flex items-center">
        <div className="mr-4">
          <label for="amountField" className="block">Amount</label>
        </div>
        <div className="mr-10 flex items-center">
          <span className="text-gray-500">$</span>
          <input id={`amountField-${idx}`} name="amountField" type="number" min="1" className="w-full px-3 py-2 border-b focus:outline-none focus_border-blue-500" value={amountSharesFieldValue} onChange={(event) => setAmountSharesFieldValue(event.target.value)} onInput={(event) => updateAmountSharesField(event.target.value, selectedShare["sharePrice"])}></input>
        </div>
        <div className="mr-6">
          <label for="sharesField" className="block">Shares</label>
        </div>
        <div>
          <input id={`sharesField-${idx}`} name="sharesField" type="number" min="0" step="0.001" className="w-full px-3 py-2 border-b focus:outline-none focus_border-blue-500" value={sharesFieldValue} onChange={(event) => setSharesFieldValue(event.target.value)} onInput={(event) => updateSharesField(event.target.value, selectedShare["sharePrice"])}></input>
        </div>
      </div>
      {showNotEnoughSharesMsg ? <p className="text-red-800 mt-5">You don't have enough shares to make this trade</p> : ''}
      <div className="mt-3 text-right">
        <input type="button" className={`rounded-full text-white bg-black p-1 text-lg w-1/5 ${showNotEnoughSharesMsg ? "disabled:opacity-50" : "hover:cursor-pointer"}`} onClick={() => { handleClickOnActionButton() ; handleCloseWindow(); }} value={actionType === "buy" ? "Buy Shares" : "Sell Shares"} disabled={showNotEnoughSharesMsg}></input>
      </div>
    </div>
  );
}
