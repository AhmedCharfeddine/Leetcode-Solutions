class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost)
        dp = [0] * len(cost)
        dp[-1], dp[-2] = cost[-1], cost[-2]
        i = len(cost) - 3
        while i >= 0:
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])
            i -= 1
        return min(dp[0], dp[1])