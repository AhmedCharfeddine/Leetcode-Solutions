class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = list(map(lambda x: -x, piles))
        heapify(piles)
        for _ in range(k):
            heappush(piles, heappop(piles)//2)
        return -sum(piles)