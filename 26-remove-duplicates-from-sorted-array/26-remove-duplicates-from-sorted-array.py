class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:  return
        ptr1, ptr2 = 0, 1
        while ptr2 < len(nums):
            if nums[ptr1] == nums[ptr2]:
                ptr2 += 1
            else:
                nums[ptr1+1] = nums[ptr2]
                ptr1 += 1
        return ptr1 + 1