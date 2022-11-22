class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:  return len(nums)
        ptr1 = 1
        if nums[0] == nums[1]:
            repeated = True
        else:
            repeated = False
        for ptr2 in range(2, len(nums)):
            if repeated:
                if nums[ptr1] != nums[ptr2]:
                    nums[ptr1+1] = nums[ptr2]
                    ptr1 += 1
                    repeated = False
            else:
                if nums[ptr1] == nums[ptr2]:
                    repeated = True
                nums[ptr1+1] = nums[ptr2]
                ptr1 += 1
        return ptr1+1