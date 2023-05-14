class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order = {order[i]: i for i in range(26)}
        return words == sorted(words, key=lambda x: tuple(order[i] for i in x))