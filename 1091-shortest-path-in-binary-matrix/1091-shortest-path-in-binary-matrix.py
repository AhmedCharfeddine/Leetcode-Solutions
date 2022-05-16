class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        steps = 1
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        if len(grid) == 1:
            return 1
        visited = {(0, 0)}
        offsets = [(x, y) for x in range(-1, 2) for y in range(-1, 2)]
        def get_neighbors(x, y):
            for x_offset, y_offset in offsets:
                new_x = x + x_offset
                new_y = y + y_offset
                if 0 <= new_x < n and 0 <= new_y < n and (new_x, new_y) not in visited and grid[new_x][new_y] == 0:
                    yield (new_x, new_y)
                
        q = [(0,0)]
        while q:
            for _ in range(len(q)):
                x,y = q.pop(0)
                
                if x==n-1 and y==n-1:
                    return steps
                
                for neighbor in get_neighbors(x, y):
                    q.append(neighbor)
                    visited.add(neighbor)
                    
            steps += 1
            
        return -1