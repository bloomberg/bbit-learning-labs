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

import ShareSuggestion from "@/components/ShareSuggestion";
import SearchBarCloseButton from "./SearchBarCloseButton";
import { useEffect, useState, useRef } from "react";
import useSWR from "swr";

const fetcher = (...args) => fetch(...args).then((res) => res.json());

export default function SearchBar() {
  const { data, error } = useSWR(`${process.env.NEXT_PUBLIC_API_URL}/get_share_names`, fetcher);
  const stockNames = data ? data["records"] : [];
  const [enableShareDropdown, setEnableShareDropdown] = useState(false);
  const stockInputRef = useRef(null);
  const [stockFieldValue, setShareFieldValue] = useState('');
  const [stockSuggestions, setstockSuggestions] = useState([]);

  function onShareFieldInput(event) {
    const input = event.target.value;
    if (!input) {
      return;
    }

    const _stockSuggestions = stockNames.filter(share => {
      return share["shareSymbol"].toLowerCase().includes(input.toLowerCase());
    });
    setstockSuggestions(_stockSuggestions.slice(0, 20));
    setEnableShareDropdown(true);
    resetSelectedShare();
  }

  function handleClickOutside(event) {
      if (stockInputRef.current && !stockInputRef.current.contains(event.target)) {
        setEnableShareDropdown(false);
    }
  }

  function updateShareFieldValue(value) {
    setShareFieldValue(value);
  }

  useEffect(() => {
    document.addEventListener("click", handleClickOutside);

    return () => {
      document.removeEventListener("click", handleClickOutside)
    };
  }, []);

  return (
    <div ref={stockInputRef} className="relative">
      {/* Work here */}
      <input className="border border-slate-300 rounded-md w-full hover: placeholder:text-slate-300 p-3 mb-3" type="text" placeholder="Search stocks to buy"></input>
      <SearchBarCloseButton></SearchBarCloseButton>
      <div id="stock-dropdown" className={`w-full max-h-60 border border-gray-300 rounded-md bg-white absolute overflow-y-auto ${!enableShareDropdown ? "hidden" : ''}`}>
        {stockSuggestions.map(share => <ShareSuggestion symbol={share["shareSymbol"]} name={share["shareName"]} updateShareField={updateShareFieldValue} disableShareDropdown={setEnableShareDropdown} updateSelectedShare={updateSelectedShare}></ShareSuggestion>)}
      </div>
    </div>
  );
}
