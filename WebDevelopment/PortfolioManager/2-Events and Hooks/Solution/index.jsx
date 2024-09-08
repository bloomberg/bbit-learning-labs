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
import { useEffect } from "react";
import Share from "@/components/Share";
import SearchBar from "@/components/SearchBar";


export default function Home() {
  const [hardCodedPortfolioValue, setHardCodedPortfolioValue] = useState(10_000);
  const [hardCodedUserAmount, setHardCodedUserAmount] = useState(10_000);

  // Create an object to store the shares of a user, as well as a hook to modify its value
  const [shares, setShares] = useState([]);
  // Create a way of keeping track if data from the backend is still loading
  const [isLoading, setLoading] = useState(true);
  // Create an object to store the selected share, as well as a hook to modify it
  const [selectedShare, setSelectedShare] = useState(null);

  // Create a flag for whether to reveal a share buy window
  const [revealBuyWindow, setRevealBuyWindow] = useState(false);

  async function updateSelectedShare(shareSymbol, shareName) {
    if (!shareSymbol) {
      return;
    }

    // Make call to backend to retrieve share information
    fetch(`http://localhost/wp-json/techlabs/v1/get_share_price/${shareSymbol}`)
      .then(res => res.json())
      .then(data => {
        const sharePrice = data;
        setSelectedShare({ symbol: shareSymbol, name: shareName, sharePrice });
      });
  }

  function resetSelectedShare() {
    setSelectedShare(null);
  }

  function handleOpenSelectedShareWindow() {
    setRevealBuyWindow(true);
  }

  function updatePortfolioValue({ shareAmount, newPortfolioValue }) {
    setHardCodedPortfolioValue(newPortfolioValue);
  }

  // Load all shares owned by current user
  useEffect(() => {
    fetch(`${process.env.NEXT_PUBLIC_API_URL}/get_shares`)
      .then((res) => res.json())
      .then((data) => {
        const _shares = data;
        setShares(_shares);
        setLoading(false);
      })
      .catch(error => {
        console.log(error);
      });
  });

  return (
    <>
      <div className="mx-auto max-w-screen-xl p-4 border border-slate-400 rounded-sm">
        <h1 className="text-5xl font-bold text-gray-900 mb-10">Portfolio Manager</h1>
        <h3 className="text-xl font-bold text-gray-900">Your Value</h3>
        <h2 className="text-4xl text-gray-900 mb-5">${hardCodedPortfolioValue.toLocaleString("en-US")}</h2>
        <div className="text-base">
          <span className="text-1xl text-gray-900 font-bold">Available to Spend: </span>${hardCodedUserAmount.toLocaleString("en-US")}
        </div>
        <h3 className="text-3xl text-gray-900 mt-12 mb-3 font-bold">Your Portfolio</h3>
        <SearchBar updateSelectedShare={updateSelectedShare} resetSelectedShare={resetSelectedShare} />
        <div className="overflow-x-auto">
          <div className={`border-collapse border-y-2  border-y-black text-sm text-left rtl:text-right text-black grid grid-cols-7 grid-rows-1`}>
            <div className="text-cs text-black bg-black contents">
              <div className="border-y border-black px-6 py-3">Name</div>
              <div className="border-y border-black px-6 py-3">Share Price</div>
              <div className="border-y border-black px-6 py-3">1D Change</div>
              <div className="border-y border-black px-6 py-3">Your Shares</div>
              <div className="border-y border-black px-6 py-3">Avg Price</div>
              <div className="border-y border-black px-6 py-3">Mkt Value</div>
              <div className="border-y border-black px-6 py-3">Your Change</div>
            </div>
            <div className="contents">
              { <Share /> }
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
