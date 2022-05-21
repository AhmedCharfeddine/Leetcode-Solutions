class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        dp = [0] + [math.inf] * amount # how many coins needed to make i amount
        
        for i in range(1, amount+1):
            if i in coins:
                dp[i] = 1
                continue
            for coin in coins:
                if i > coin and dp[i-coin] != -1:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
            
        return dp[-1] if dp[-1] + 1 != dp[-1] else -1