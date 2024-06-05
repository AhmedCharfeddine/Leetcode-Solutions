class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) == 1:
            return list(words[0])
        
        commons = Counter(words[0])
        for word in words[1:]:
            cur_count = Counter(word)
            for char in commons:
                commons[char] = min(commons[char], cur_count.get(char, 0))
        
        res = []
        for char in commons:
            res.extend([char] * commons[char])
            
        return res