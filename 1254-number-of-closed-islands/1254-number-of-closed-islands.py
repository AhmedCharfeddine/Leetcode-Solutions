class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        offset = {(-1, 0), (1, 0), (0, -1), (0, 1)}
        def get_neighbors(x,y):
            for x_offset, y_offset in offset:
                x_new = x + x_offset
                y_new = y + y_offset
                if 0 <= x_new < n and 0 <= y_new < m and grid[x_new][y_new] == 0 and (x_new, y_new) not in visited:
                    yield (x_new, y_new)
        
        n, m = len(grid), len(grid[0])
        visited = set()
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 and (i,j) not in visited:
                    # perform dfs
                    is_island = True    # switch to False if border found
                    if i in [0, n-1] or j in [0, m-1]:  
                        is_island = False
                    stack = deque([(i,j)])
                    while stack:
                        x,y = stack.pop()
                        for x_neighbor,y_neighbor in get_neighbors(x,y):
                            if x_neighbor in [0,n-1] or y_neighbor in [0,m-1]:
                                is_island = False
                            stack.append((x_neighbor,y_neighbor))
                        visited.add((x,y))
                    if is_island:   
                        res += 1
        return res