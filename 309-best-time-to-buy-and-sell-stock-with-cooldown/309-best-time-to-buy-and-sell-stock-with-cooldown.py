class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:    return 0
        dp = []
        for _ in range(len(prices)):
            dp.append([None, None])
        
        def dfs(i, turn):
            if i >= len(prices): return 0
            '''
            0 for the player already bought: either sell or do nothing
            1 for cooldown: either do nothing or buy
            '''

            if dp[i][turn] is None:
                if turn == 0:
                    dp[i][turn] = max(prices[i] + dfs(i+2, 1), dfs(i+1, 0))
                elif turn == 1:
                    dp[i][turn] = max(dfs(i+1, 1), -prices[i] + dfs(i+1, 0))
            return dp[i][turn]
        
        
        return dfs(0, 1) # no need for dfs(0, 0) since you can't sell on the first day 