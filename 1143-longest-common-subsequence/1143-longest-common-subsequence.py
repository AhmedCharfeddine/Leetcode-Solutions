class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = []
        for _ in range(m):  dp.append([0]*n)
        for i in range(m):
            for j in range(n):
                if 0 in (i,j):  
                    if i != 0:
                        dp[i][j] = dp[i-1][j]
                    elif j != 0:
                        dp[i][j] = dp[i][j-1]
                    dp[i][j] = max(dp[i][j], int(text1[i] == text2[j]))
                else:
                    if text1[i] == text2[j]:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]