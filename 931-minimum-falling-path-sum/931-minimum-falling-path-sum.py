class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n == 1:  return matrix[0][0]
        dp = []
        for _ in range(n-1):    dp.append([0]*n)
        dp.append(matrix[-1])
        
        offset = ((1,-1), (1,0), (1,1))
        def get_neighbors(i, j):
            for x_offset, y_offset in offset:
                x_new = i + x_offset
                y_new = j + y_offset
                if 0 <= x_new < n and 0 <= y_new < n:
                    yield x_new,y_new
        
        for i in range(n-2, -1, -1):
            for j in range(n):
                dp[i][j] = matrix[i][j] + min(dp[x][y] for x,y in get_neighbors(i,j))
        
        return min(dp[0])