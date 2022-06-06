class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return min(nums)
        start, stop = 0, n-1
        
        while nums[start] == nums[stop] and start != stop:
            start += 1
        while stop - start > 1:
            pos = math.ceil((start+stop)/2)
            
            if nums[pos] > nums[stop]:
                start = pos
            else:
                stop = pos
            
        return min(nums[start], nums[stop])