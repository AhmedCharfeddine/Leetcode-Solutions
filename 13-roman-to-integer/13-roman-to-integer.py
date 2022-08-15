class Solution:
    def romanToInt(self, s: str) -> int:
        rti = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, '': 0}
        
        def helper(string, res):
            if len(string) <= 1:
                return rti[string] + res
            
            if (string[0] == 'I' and string[1] in 'XV') or \
                (string[0] == 'X' and string[1] in 'LC') or \
                (string[0] == 'C' and string[1] in 'DM'):
                    start = 2
                    res += rti[string[1]] - rti[string[0]]
            else:
                start = 1
                res += rti[string[0]]
            return helper(string[start:], res)
        return helper(s, 0)