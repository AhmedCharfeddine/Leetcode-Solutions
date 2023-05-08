class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if max(nums) >= target: return 1
        if len(nums) < 2:
            return 1 if sum(nums) >= target else 0
        
        res = math.inf
        left, right = 0, 1
        s = nums[left]
        while right < len(nums):
            if s < target:
                # expand window
                s += nums[right]
                right += 1
                
            else:
                # update res
                res = min(res, right - left)
                
                # shrink window
                if left == right - 1:
                    left += 1
                    right += 1
                    s = nums[left]
                else:
                    s -= nums[left]
                    left += 1
        
        # keep shrinking window and updating res
        while left < right and s >= target:
            res = min(res, right - left)
            s -= nums[left]
            left += 1

        # if no result found
        if res == res + 1:
            return 0
        return res