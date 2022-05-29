class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr1, ptr2 = 0, len(nums) - 1
        while ptr1 != ptr2:
            if nums[ptr1] != 0:
                ptr1 += 1
            else:
                nums.pop(ptr1)
                ptr2 -= 1
                nums.append(0)
        