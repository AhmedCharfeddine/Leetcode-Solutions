class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_buy, res = prices[0], 0
        for i in range(len(prices)):
            res = max(res, prices[i]-best_buy)
            best_buy = min(best_buy, prices[i])
        return res