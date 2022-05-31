class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if len(s) == 1: return [1]
        res = []
        ptr1, ptr2, ptr3 = 0, len(s) - 1, -1
        last_appearances = {}
        while ptr1 < len(s):
            ptr2 = len(s) - 1
            if s[ptr1] not in last_appearances:
                while s[ptr1] != s[ptr2] and ptr1 <= ptr2:
                    ptr2 -= 1
                last_appearances[s[ptr1]] = ptr2
            else:
                ptr2 = last_appearances[s[ptr1]]
            if ptr2 > ptr3:
                ptr3 = ptr2
            if ptr1 == ptr3:
                res.append(ptr1 - sum(res) + 1)
                
            ptr1 += 1
            
        return res