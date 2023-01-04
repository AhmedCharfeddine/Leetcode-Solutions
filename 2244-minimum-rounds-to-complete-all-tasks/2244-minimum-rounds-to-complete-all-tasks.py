class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        hm = Counter(tasks)
        res = 0
        dp = [None, None, 1, 1, 2, 2, 2, 3]
        for diff in hm.values():
            if diff == 1:   return -1
            while diff >= len(dp):
                if len(dp) % 3 == 0:
                    dp.append(dp[-3]+1)
                elif len(dp) % 3 == 1:
                    dp.append(dp[-1]+1)
                else:
                    dp.append(dp[-2]+1)
            res += dp[diff]
        return res