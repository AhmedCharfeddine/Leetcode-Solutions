class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for s in strs:
            tup = tuple(sorted(s))
            if tup in hm:
                hm[tup].append(s)
            else:
                hm[tup] = [s]
        return hm.values()