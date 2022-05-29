class Solution:
    def maxArea(self, height: List[int]) -> int:
        ptr1, ptr2 = 0, len(height) - 1
        res = -1 * math.inf
        while ptr1 < ptr2:
            res = max(res, min(height[ptr1], height[ptr2]) * (ptr2 - ptr1))
            if height[ptr1] < height[ptr2]:
                ptr1 += 1
            else:
                ptr2 -= 1
        return res