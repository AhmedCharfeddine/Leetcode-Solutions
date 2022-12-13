class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n == 1:  return matrix[0][0]
        dp = []
        for _ in range(n-1):    dp.append([0]*n)
        dp.append(matrix[-1])
        
        def get_neighbors(i, j):
            for y in range(n):
                if y != j:
                    yield i+1, y 
        
        for i in range(n-2, -1, -1):
            for j in range(n):
                dp[i][j] = matrix[i][j] + min(dp[x][y] for x,y in get_neighbors(i,j))
        
        return min(dp[0])