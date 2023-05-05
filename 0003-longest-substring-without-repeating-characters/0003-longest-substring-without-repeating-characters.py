class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 2: return len(set(s))
        res = 1
        ptr1, ptr2 = 0, 1
        cur_substring = {s[0]}
        while ptr2 < len(s):
            if s[ptr2] not in cur_substring:
                cur_substring.add(s[ptr2])
                res = max(res, len(cur_substring))
                ptr2 += 1
            else:
                cur_substring.remove(s[ptr1])
                if ptr1 + 1 == ptr2:
                    ptr2 += 1
                    cur_substring.add(s[ptr1+1])
                ptr1 += 1
        return res