class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2:   return n
        ptr1, ptr2 = 0, 1
        hm = {s[0]:1}
        res = 0
        while ptr2 < n:
            # add char count to dict
            hm[s[ptr2]] = hm.get(s[ptr2], 0) + 1
            
            # shrink window
            while ptr2-ptr1+1 != len(hm):
                hm[s[ptr1]] -= 1
                if hm[s[ptr1]] == 0:
                    hm.pop(s[ptr1])
                ptr1 += 1
            
            res = max(res, len(hm))
            ptr2 += 1
        return res