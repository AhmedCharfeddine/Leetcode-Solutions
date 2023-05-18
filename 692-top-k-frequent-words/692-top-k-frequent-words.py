class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = Counter(words)
        return sorted(d.keys(), key=lambda x: (-d[x], x))[:k]