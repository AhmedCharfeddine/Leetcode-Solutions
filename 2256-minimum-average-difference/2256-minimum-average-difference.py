class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        if len(nums) <= 1:  return 0
        left_sum, right_sum = 0, sum(nums)
        n = len(nums)
        min_avg, res = math.inf, -1
        for i in range(n):
            right_sum -= nums[i]
            left_sum += nums[i]
            left_avg, right_avg = int(left_sum/(i+1)), int(right_sum/max(1,n-i-1))
            avg_diff = abs(left_avg - right_avg)
            if avg_diff < min_avg:
                min_avg = avg_diff
                res = i
        return res