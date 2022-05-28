class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = set(nums)
        for i in range(len(nums)+1):
            try:
                s.remove(i)
            except:
                return i