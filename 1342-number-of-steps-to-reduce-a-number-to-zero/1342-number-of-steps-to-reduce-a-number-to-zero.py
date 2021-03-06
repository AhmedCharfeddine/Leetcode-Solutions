class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        res = 0
        while True:
            if num == 1:
                return res + 1
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            res += 1