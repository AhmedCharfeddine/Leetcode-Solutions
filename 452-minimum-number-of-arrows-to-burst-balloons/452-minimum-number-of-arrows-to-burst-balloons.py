class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        res, interval_end = 0, -math.inf
        for start, end in points:
            if interval_end < start:
                res += 1
                interval_end = end
        return res