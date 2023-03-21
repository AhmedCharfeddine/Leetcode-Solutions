class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        subarray_len = 0
        cur_subarray_count = 0
        res = 0
        for i in nums:
            subarray_len = subarray_len + 1 if not i else 0
            if subarray_len:
                cur_subarray_count += subarray_len
            else:
                res += cur_subarray_count
                cur_subarray_count = 0
        return res + cur_subarray_count