class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:  return True
        dp = [False] * len(nums)
        dp[-1] = True
        for i in range(len(nums)-2, -1, -1):
            dp[i] = any(dp[i:i+nums[i]+1])
        return dp[0]