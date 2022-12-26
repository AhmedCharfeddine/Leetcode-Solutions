class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:  return True
        dp = [False] * len(nums)
        dp[-1] = True
        for i in range(len(nums)-2, -1, -1):
            for j in range(min(len(nums)-1,i+nums[i]), i, -1):
                if dp[j]:
                    dp[i] = True
                    break
        return dp[0]