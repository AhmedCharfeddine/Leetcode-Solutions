class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        freq1 = Counter(word1)
        freq2 = Counter(word2)
        if not freq1.keys() == freq2.keys():    return False
        return Counter(freq1.values()) == Counter(freq2.values())