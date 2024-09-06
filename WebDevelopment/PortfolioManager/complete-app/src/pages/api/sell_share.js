// Next.js API route support: https://nextjs.org/docs/api-routes/introduction

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
