class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        cur_h, cur_s = map(int, current.split(':'))
        cor_h, cor_s = map(int, correct.split(':'))
        diff = (cor_h-cur_h)*60 + (cor_s-cur_s)
        res = 0
        
        for time_jump in [60, 15, 5, 1]:
            if diff >= time_jump:
                res += diff // time_jump
                diff = diff % time_jump
        return res 