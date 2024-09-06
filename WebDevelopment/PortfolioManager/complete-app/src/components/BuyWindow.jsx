import BuySellWindow from "@/components/BuySellWindow";

export default function BuyWindow({
  selectedShare,
  handleCloseWindow,
  idx,
  hardCodedUserAmount,
  setHardCodedUserAmount,
  portfolioValue,
  updatePortfolioValue
}) {
  async function handleBuySelectedShare({ shareSymbol, shareAmount, shareCount }) {
    const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/buy_share/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        shareSymbol,
        shareAmount: parseFloat(shareAmount),
        shareCount: parseFloat(shareCount),
        hardCodedUserAmount,
        portfolioValue
      })
    });
    const data = await response.json();
    const { newAmount, newPortfolioValue } = data;
    setHardCodedUserAmount(newAmount);
    updatePortfolioValue({ shareAmount, newPortfolioValue })
  }

  return <BuySellWindow selectedShare={selectedShare} actionType="buy" handleActionSelectedShare={handleBuySelectedShare} handleCloseWindow={handleCloseWindow} idx={idx} />;
}
