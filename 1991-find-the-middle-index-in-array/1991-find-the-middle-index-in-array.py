class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:  return 0
        
        left_prefix, right_prefix = [0] * len(nums), [0] * len(nums)
        left_prefix[0] = nums[0]
        right_prefix[-1] = nums[-1]
        
        for i in range(1, len(nums)-1):
            left_prefix[i] = left_prefix[i-1] + nums[i]
            right_prefix[-i-1] = right_prefix[-i] + nums[-i-1]
        
        left_prefix[-1] = left_prefix[-2] + nums[-1]
        right_prefix[0] = right_prefix[1] + nums[0]
        
        for i in range(len(nums)):
            if left_prefix[i] == right_prefix[i]:
                return i
        return -1