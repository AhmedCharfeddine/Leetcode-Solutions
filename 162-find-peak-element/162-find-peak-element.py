class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:  return 0
        if len(nums) == 2:
            return nums.index(max(nums))
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums)-1
        def helper(nums, start, end):
            if end-start > 1:
                mid = (start+end)//2
                if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                    return mid
                r1 = helper(nums, start, mid)
                if r1:  return r1
                return helper(nums, mid, end)
        return helper(nums, 0, len(nums)-1)