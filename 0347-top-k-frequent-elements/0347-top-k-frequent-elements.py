class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return sorted(count.keys(), key=lambda x: count[x], reverse=True)[:k]