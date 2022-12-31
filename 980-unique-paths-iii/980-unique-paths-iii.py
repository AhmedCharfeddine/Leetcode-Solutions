class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        white_blocks = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    white_blocks += 1
                elif grid[i][j] == 1:
                    start = (i,j)
                elif grid[i][j] == 2:
                    end = (i,j)
                    
                    
        offset = {(-1,0), (1,0), (0,-1), (0,1)}
        def get_neighbors(x,y):
            for x_offset, y_offset in offset:
                i, j = x+x_offset, y+y_offset
                if (0 <= i < n and 0 <= j < m and (i,j) not in visited):
                    if grid[i][j] == 0:
                        yield (i,j)
                    elif grid[i][j] == 2 and len(visited) == white_blocks:
                        yield(i,j)
        
        visited = set()
        def dfs(square):
            if square == end:
                return 1
            res = 0
            for i,j in get_neighbors(*square):
                visited.add((i,j))
                res += dfs((i,j))
                visited.remove((i,j))
            return res
        return dfs(start)
            