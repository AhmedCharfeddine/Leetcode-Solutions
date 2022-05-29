class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:  return [nums[0] ** 2]
        ptr1, ptr2 = 0, len(nums) - 1
        res = []
        while (ptr1 < len(nums) and nums[ptr1] < 0) or (ptr2 >= 0 and nums[ptr2] >= 0):
            if nums[ptr1] >= 0 or nums[ptr2] < 0:
                if nums[ptr1] >= 0:
                    res.insert(0, nums[ptr2] ** 2)
                    ptr2 -= 1
                else:
                    res.insert(0, nums[ptr1] ** 2)
                    ptr1 += 1 
            elif - nums[ptr1] > nums[ptr2]:
                res.insert(0, nums[ptr1] ** 2)
                ptr1 += 1
            else:
                res.insert(0, nums[ptr2] ** 2)
                ptr2 -= 1
                
                
        return res