class Solution:
    def intToRoman(self, num: int) -> str:
        table = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        conversions = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M', 4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}
        res = []
        
        while num != 0:
            pos = 0
            while table[pos] > num:
                pos += 1
            num -= table[pos]
            res.append(conversions[table[pos]])
        
        return ''.join(res)