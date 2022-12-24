class Solution:
    def numTilings(self, n: int) -> int:
        '''
        The states are inspired from:
        https://www.youtube.com/watch?v=CecjOo4Zo-g
        '''
        if n == 1:  return 1
        dp = []
        for _ in range(n):
            dp.append([None]*2)
        dp[-1] = [1, 1]
        dp[-2] = [2, 1]
        def dfs(i, state):
            if dp[i][state] is not None:
                return dp[i][state]
            if state == 0:      # both vertical cells are empty
                dp[i][state] = int((dfs(i+2, 0) + dfs(i+1, 0) + 2*dfs(i+1, 1)) % (1e9+7))
            elif state == 1:    # bottom OR top vertical cell is empty
                dp[i][state] = int((dfs(i+2, 0) + dfs(i+1, 1)) % (1e9+7))
            return dp[i][state]
        dfs(0,0)
        return int(dp[0][0] % (1e9+7))