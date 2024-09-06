// Next.js API route support: https://nextjs.org/docs/api-routes/introduction

export default async function handler(req, res) {
    const shareSymbol = req.query.symbol;
    if (shareSymbol) {
        const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}:${process.env.NEXT_PUBLIC_API_PORT}/get_percentage_change/${shareSymbol}`);
        const sharePercentChangeStr = await response.text();
        const sharePercentChange = Number(sharePercentChangeStr.replace(/%/, ''));
        return res.status(200).json({ sharePercentChange });
    } else {
        return res.status(500).send({ error: "Invalid share symbol." });
    }
}
