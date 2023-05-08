class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prefix, right_prefix = [0] * len(nums), [0] * len(nums)
        left_prefix[0] = nums[0]
        right_prefix[-1] = nums[-1]
        
        for i in range(1, len(nums)-1):
            left_prefix[i] = left_prefix[i-1] * nums[i]
            right_prefix[-i-1] = right_prefix[-i] * nums[-i-1]
        
        left_prefix[-1] = left_prefix[-2] * nums[-1]
        right_prefix[0] = right_prefix[1] * nums[0]
        
        res = [0] * len(nums)
        res[0] = right_prefix[1]
        res[-1] = left_prefix[-2]
        
        for i in range(1, len(nums)-1):
            res[i] = left_prefix[i-1] * right_prefix[i+1]
        
        
        return res