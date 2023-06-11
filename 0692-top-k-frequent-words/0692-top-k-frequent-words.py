class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        sorted_items = sorted(count.items(), key=lambda item: (-item[1], item[0]))
        return list(map(lambda item: item[0], sorted_items))[:k]