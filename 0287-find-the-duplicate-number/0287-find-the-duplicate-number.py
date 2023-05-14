class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        occ = set()
        for i in nums:
            if i in occ:
                return i
            occ.add(i)