class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for index, elt in enumerate(nums):
            if elt in hm:
                return (index, hm[elt])
            hm[target-elt] = index
