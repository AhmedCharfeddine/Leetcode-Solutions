class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return nums.index(target) if target in nums else -1
        if nums[0] == target:   return 0
        if nums[-1] == target:  return len(nums) - 1
        def helper(start, end):
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if end - start > 1:
                if nums[start] > nums[mid]:
                    # break is to the left
                    if nums[mid] < target <= nums[end]:
                        return helper(mid, end)
                    else:
                        return helper(start, mid)
                elif nums[end] < nums[mid]:
                    # break is to the right
                    if nums[start] <= target < nums[mid]:
                        return helper(start, mid)
                    else:
                        return helper(mid, end)
                else:
                    # table is not rotated
                    if target < nums[mid]:
                        return helper(start, mid)
                    else:
                        return helper(mid, end)
            else:   
                return -1    
        return helper(0, len(nums)-1)
    
    