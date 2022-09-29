class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == 1:   return arr
        ptr1, ptr2 = 0, len(arr) - 1
        while ptr2-ptr1 >= k:
            if abs(arr[ptr1] - x) <=  abs(arr[ptr2] - x):
                ptr2 -= 1
            else:
                ptr1 += 1
        return arr[ptr1:ptr2+1]