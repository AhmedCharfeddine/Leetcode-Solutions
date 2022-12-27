class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        remaining = sorted([capacity[i] - rocks[i] for i in range(len(rocks))])
        res, i = 0, 0
        while i < len(rocks) and additionalRocks >= remaining[i]:
            additionalRocks -= remaining[i]
            i += 1
            res += 1
        return res