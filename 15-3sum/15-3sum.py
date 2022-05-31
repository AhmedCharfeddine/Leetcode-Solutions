class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:   return []
        nums.sort()
        ptr1 = 0
        res = []
        while (nums[ptr1] < 0) and (ptr1 < len(nums) - 2):
            if ptr1 != 0 and nums[ptr1] == nums[ptr1 - 1]:
                print(ptr1)
                ptr1 += 1
                continue
            ptr2, ptr3 = ptr1 + 1, len(nums) - 1
            while ptr2 < ptr3:
                s = nums[ptr1] + nums[ptr2] + nums[ptr3]
                if s == 0:
                    res.append([nums[ptr1], nums[ptr2], nums[ptr3]])
                    ptr3 -= 1
                    while nums[ptr3] == nums[ptr3+1] and ptr2 < ptr3:
                        ptr3 -= 1
                elif s < 0:
                    ptr2 += 1
                    while nums[ptr2] == nums[ptr2-1] and ptr2 < ptr3:
                        ptr2 += 1
                else:
                    ptr3 -= 1
                    while nums[ptr3] == nums[ptr3+1] and ptr2 < ptr3:
                        ptr3 -= 1
            ptr1 += 1
        
        # ptr1 is at index of the first positive or zero value
        if ptr1 < len(nums) - 2 and nums[ptr1:ptr1+3] == [0, 0, 0]:
            res.append([0, 0, 0])
        return res