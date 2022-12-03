class Solution:
    def frequencySort(self, s: str) -> str:
        hm = {}
        for i in s: hm[i] = hm.get(i, 0) + 1
        res = []
        for char,freq in sorted(hm.items(), key=lambda x: x[1], reverse=True):
            res.extend([char]*freq)
        return ''.join(res)