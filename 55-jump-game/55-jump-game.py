class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:  return True
        dp = [False] * len(nums)
        dp[-1] = True
        for i in range(len((nums))-2, -1, -1):
            if True in dp[i+1:i+nums[i]+1]:
                dp[i] = True
        return dp[0]