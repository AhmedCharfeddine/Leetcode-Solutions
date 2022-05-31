class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = math.inf
        ptr1 = 0
        while ptr1 < len(nums) - 2:
            ptr2, ptr3 = ptr1+1, len(nums)-1
            while ptr2 != ptr3:
                s = nums[ptr1] + nums[ptr2] + nums[ptr3]
                if s == target:
                    return s
                if abs(s - target) < abs(res - target):
                    res = s
                if s < target:
                    ptr2 += 1
                else:
                    ptr3 -= 1
            ptr1 += 1
        return res