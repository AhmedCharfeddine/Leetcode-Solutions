class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return min(nums)
        start, stop = 0, n-1
        while True:
            pos = math.ceil((start+stop)/2)
            if pos == n-1:  return nums[0]
            if stop - start == 1:   return min(nums[start], nums[stop])
            if nums[pos] > nums[pos+1]:
                return nums[pos+1]
            elif nums[pos] > nums[stop]:
                start = pos
            else:
                stop = pos
                