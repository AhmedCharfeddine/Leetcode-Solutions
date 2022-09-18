class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:  return 0
        res = 0
        dp_left = [height[0]] + [-1] * (n-2) + [height[-1]]
        dp_right = [height[0]] + [-1] * (n-2) + [height[-1]]
        
        for i in range(1, n-1):
            dp_left[i] = max(dp_left[i-1], height[i])
            dp_right[-i-1] = max(dp_right[-i], height[-i-1])
        
        
        for i in range(1, n-1):
            left_max = dp_left[i]
            right_max = dp_right[i]
            if left_max > height[i] and right_max > height[i]:
                res += min(left_max, right_max) - height[i]
        
        return res