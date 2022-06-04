class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s = nums[0]
        best = math.inf
        ptr1, ptr2 = 0, 0
        while True:
            while s < target or ptr1 == ptr2:
                if nums[ptr2] >= target:
                    return 1
                ptr2 += 1
                if ptr2 == len(nums):
                    if best == best+1:
                        if s >= target:
                            return len(nums)
                        return 0
                    return best
                s += nums[ptr2]
            best = min(best, ptr2-ptr1+1)
            while s >= target and ptr1 < ptr2:
                ptr1 += 1
                s -= nums[ptr1-1]
                if s >= target:
                    best = min(best, ptr2-ptr1+1)
