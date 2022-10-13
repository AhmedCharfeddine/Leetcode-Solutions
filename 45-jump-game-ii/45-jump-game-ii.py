class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:  return 0
        '''
        [2,3,1,1,4]
        [i,i,2,1,0]
        min([nums[i + it]+it for it in range(1, nums[i]+1)])
        '''
        dp = [math.inf] * len(nums)
        dp[-1] = 0
        for i in range(len(nums)-2, -1, -1):
            if nums[i] == 0:
                continue
            reach = min(len(nums)-1, i+nums[i])
            dp[i] = 1 + min(dp[j] for j in range(i+1, reach+1))
        return dp[0]