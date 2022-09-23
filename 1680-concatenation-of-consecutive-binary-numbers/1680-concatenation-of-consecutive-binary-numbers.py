class Solution:
    def concatenatedBinary(self, n: int) -> int:
        if n == 1:  return 1
        res, MOD = 1, 1e9+7
        bits = 2
        
        for i in range(2, n+1):
            res <<= len(format(i,'b'))
            res = int((res + i) % MOD)
        
        return res