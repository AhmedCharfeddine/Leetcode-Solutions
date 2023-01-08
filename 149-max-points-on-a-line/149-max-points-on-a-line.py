class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 3: return len(points)
        lines = set()
        res = min(len(points), 2)
        for i in range(len(points)-2):
            x1, y1 = points[i]
            for j in range(i+1, len(points)-1):
                x2, y2 = points[j]
                try:
                    slope = (y2-y1)/(x2-x1)
                    b0 = y1-slope*x1
                except ZeroDivisionError:
                    slope = None
                    b0 = x1
                if (slope, b0) not in lines:
                    lines.add((slope,b0))
                    cur_count = 2   # count of points on the current line
                    for k in range(j+1, len(points)):
                        x3, y3 = points[k]
                        if ((slope is None and x3 == b0)                    # vertical slope
                            or (slope is not None and isclose(y3, slope*x3+b0))):  # not vertical
                            cur_count += 1
                    res = max(res, cur_count)
        print(lines)
        return res