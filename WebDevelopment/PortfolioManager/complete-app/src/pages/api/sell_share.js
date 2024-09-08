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
        shareCount,
        hardCodedUserAmount,
        portfolioValue,
    } = req.body;

    const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}:${process.env.NEXT_PUBLIC_API_PORT}/sell_share`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            shareCount
        })
    });

    const sharePriceResponse = await fetch(`${process.env.NEXT_PUBLIC_API_URL}:${process.env.NEXT_PUBLIC_API_PORT}/get_share_price/${shareSymbol}`);
    const sharePrice = Number((await sharePriceResponse.text()).replace(/[^0-9.-]+/g, ''));
    const marketValue = shareCount * sharePrice;
    const newAmount  = hardCodedUserAmount + marketValue;
    const newPortfolioValue = parseFloat(
        (portfolioValue - marketValue).toFixed(3)
    );

    return res.status(200).json({ newAmount, newPortfolioValue });
}
