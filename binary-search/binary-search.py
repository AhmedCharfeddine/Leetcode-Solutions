class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) <= 2:
            return nums.index(target) if target in nums else -1
        start, end = 0, len(nums) - 1
        while end - start > 1:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                end = mid
            else:
                start = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1