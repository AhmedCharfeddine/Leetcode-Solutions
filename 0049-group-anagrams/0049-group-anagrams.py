class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for word in strs:
            count = tuple(sorted(Counter(word).items()))
            if count in res:
                res[count].append(word)
            else:
                res[count] = [word]
        return res.values()