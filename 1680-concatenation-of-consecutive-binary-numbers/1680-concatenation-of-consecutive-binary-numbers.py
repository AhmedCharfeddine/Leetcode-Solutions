class Solution:
    def concatenatedBinary(self, n: int) -> int:
        if n == 1:  return 1
        res, MOD = 1, 1e9+7
        bits = 2
        
        for i in range(2, n+1):
            res <<= bits
            res = int((res + i) % MOD)
            if i & (i+1) == 0:
                bits += 1

        return res