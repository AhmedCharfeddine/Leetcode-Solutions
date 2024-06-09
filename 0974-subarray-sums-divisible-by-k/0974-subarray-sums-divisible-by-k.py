class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:  return int(nums[0] % k == 0)
        prefix_sum = [nums[0] % k]
        for i in range(1, len(nums)):
            prefix_sum.append((nums[i] + prefix_sum[i-1]) % k)
        count = Counter(prefix_sum)
        res = 0
        print(prefix_sum)
        for item in count:
            if item == 0:
                res += count[item]
            if count[item] > 1:
                res += count[item] * (count[item] - 1) // 2
        return res