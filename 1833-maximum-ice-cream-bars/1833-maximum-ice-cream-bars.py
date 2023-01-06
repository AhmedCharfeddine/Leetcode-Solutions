class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        heapify(costs)
        res = 0
        while costs and coins > 0:
            coins -= heappop(costs)
            res += 1
        if coins < 0:
            return res - 1        
        if not costs:
            return res
        return res