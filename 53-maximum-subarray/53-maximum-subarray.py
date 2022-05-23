class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        cur_sum = 0
        for i in nums:
            if cur_sum <= 0:
                cur_sum = i
            else:
                cur_sum += i
            res = max(cur_sum, res)
        return res