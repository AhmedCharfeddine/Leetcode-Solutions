class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hm = {0:0}
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            if s % k not in hm:
                hm[s%k] = i + 1
            else:
                if i > hm[s%k]:
                    return True
        return False