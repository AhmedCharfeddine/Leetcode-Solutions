class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        right_max = prices[-1]
        best_buy = right_max - prices[-2] 
        for i in range(len(prices) - 2, -1, -1):
            right_max = max(right_max, prices[i])
            best_buy = max(best_buy, right_max - prices[i])
        return best_buy