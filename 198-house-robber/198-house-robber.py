class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:  return max(nums)
        dp = nums.copy()
        dp.append(-math.inf)
        for i in range(len(nums)-3, -1, -1):
            dp[i] = nums[i] + max(dp[i+2], dp[i+3])
        return max(dp[0], dp[1])