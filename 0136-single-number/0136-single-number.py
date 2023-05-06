class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        once, twice = set(), set()
        for i in nums:
            if i not in once and i not in twice:
                once.add(i)
            elif i not in twice:
                once.remove(i)
                twice.add(i)
            
        return list(once)[0]