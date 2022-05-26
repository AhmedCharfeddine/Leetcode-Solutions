class Solution:
    def hammingWeight(self, n: int) -> int:
        print(str(n))
        return bin(n).count('1')