// Next.js API route support: https://nextjs.org/docs/api-routes/introduction

export default async function handler(req, res) {
    const shareSymbol = req.query.symbol;
    if (shareSymbol) {
        const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}:${process.env.NEXT_PUBLIC_API_PORT}/get_share_price/${shareSymbol}`);
        const sharePriceString = await response.text();
        const sharePrice = Number(sharePriceString.replace(/\$(\d+)\.(\d+)/, "$1.$2"));
        return res.status(200).json({ sharePrice });
    } else {
        return res.status(500).send({ error: "Invalid share symbol." });
    }
}
