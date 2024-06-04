class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        res = 0
        for c in count:
            res += count[c] - (count[c] % 2)
        return res + int(res < len(s))