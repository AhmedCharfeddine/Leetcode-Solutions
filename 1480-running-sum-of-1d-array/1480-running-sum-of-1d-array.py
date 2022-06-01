class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        rs = 0
        res = []
        for i in nums:
            rs += i
            res.append(rs)
        return res