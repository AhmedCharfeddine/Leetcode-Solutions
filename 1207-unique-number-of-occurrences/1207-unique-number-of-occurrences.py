class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hm = {}
        for i in arr:
            hm[i] = hm.get(i, 0) + 1
        return len(hm) == len(set(hm.values()))