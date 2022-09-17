class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        reverse, res = {}, []
        
        for i, string in enumerate(words):
            reverse[string[::-1]] = i
        
        for i, str1 in enumerate(words):
            for ptr in range(len(str1)+1):
                if str1[:ptr] in reverse and str1[ptr:]==str1[:ptr-1:-1] and i != reverse[str1[:ptr]]:
                    res.append((i, reverse[str1[:ptr]]))

                if str1[ptr:] in reverse and str1[:ptr]==str1[ptr-1::-1] and reverse[str1[ptr:]] != i:
                    res.append((reverse[str1[ptr:]], i))
                    if ptr == len(str1): # one string is empty
                        res.append((i, reverse['']))
                
                        
        return res