class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if len(s) == 1: return [1]
        res = []
        ptr1, ptr2, ptr3 = 0, len(s) - 1, -1
        while ptr1 < len(s):
            ptr2 = len(s) - 1
            while s[ptr1] != s[ptr2] and ptr1 <= ptr2:
                ptr2 -= 1
            if ptr2 > ptr3:
                ptr3 = ptr2
            if ptr1 == ptr3:
                res.append(ptr1 - sum(res) + 1)
                
            ptr1 += 1
            
        return res