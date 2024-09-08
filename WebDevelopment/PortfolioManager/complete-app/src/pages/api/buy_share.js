// Next.js API route support: https://nextjs.org/docs/api-routes/introduction
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

export default async function handler(req, res) {
    const {
        shareSymbol,
        shareAmount,
        shareCount,
        portfolioValue,
        hardCodedUserAmount
    } = req.body;

    // TODO: Replace this for a call to an actual API that fetches price for a
    // particular share.
    const sharePriceResponse = await fetch(`${process.env.NEXT_PUBLIC_API_URL}:${process.env.NEXT_PUBLIC_API_PORT}/get_share_price/${shareSymbol}`);
    const sharePrice = Number((await sharePriceResponse.text()).replace(/[^0-9.-]+/g, ''));

    // TODO: Replace this for a call to an actual API that fetches percentage change
    // for a particular share.
    const sharePercentChangeResponse = await fetch(`${process.env.NEXT_PUBLIC_API_URL}:${process.env.NEXT_PUBLIC_API_PORT}/get_percentage_change/${shareSymbol}`)
    const sharePercentChange = Number((await sharePercentChangeResponse.text()).replace(/[^0-9.-]+/g, ''));

    const marketValue = parseFloat((shareCount * sharePrice).toFixed(3));

    // TODO: Have to add existing share count in API
    const share = {
        "symbol": shareSymbol,
        "sharePrice": sharePrice,
        "1dChange": sharePercentChange,
        "yourShares": shareCount,
        "avgPrice": 0,
        "mktValue": marketValue,
        "yourChange": 0
    };
    const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}:${process.env.NEXT_PUBLIC_API_PORT}/buy_share`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(share)
    });
    const data = await response.json();

    const newAmount = hardCodedUserAmount - shareAmount;
    const newPortfolioValue = parseFloat(
        (portfolioValue + sharePrice * sharePercentChange).toFixed(3)
    );
    return res.status(200).json({ newAmount, newPortfolioValue });
}
