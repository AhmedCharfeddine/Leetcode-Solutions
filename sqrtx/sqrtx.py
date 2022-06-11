class Solution:
    def mySqrt(self, x: int) -> int:
        if x in [0, 1]:  return x
        l = range(1, x)
        left, right = 0, len(l)-1
        while right - left > 1:
            mid = left + (right - left) // 2
            if l[mid] ** 2 == x:    
                return l[mid]
            if l[mid] ** 2 < x:
                left = mid
            else:
                right = mid
        return l[left]