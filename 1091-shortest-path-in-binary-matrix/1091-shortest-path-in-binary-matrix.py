class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        
        N = len(grid)
        offsets = [(x,y) for x in range(-1,2) for y in range(-1,2)]
        
        q = deque()
        q.append((0,0)) 
        visited = {(0, 0)}
        
        
        def get_neighbours(x,y):
            for x_offset, y_offset in offsets:
                new_row = x + x_offset
                new_col = y + y_offset
                
                if 0 <= new_row < N and 0 <= new_col < N and grid[new_row][new_col] == 0 and (new_row, new_col) not in visited:
                    yield (new_row, new_col)                                                
            
        
        current_distance = 1 
        
        while q:
            length = len(q)
            
            # loop through all the cells at the same distance
            for _ in range(length):
                row, col = q.popleft()
                
                if row == N-1 and col==N-1: # reached target
                    return current_distance
                
                # loop though all valid neignbours
                for p in get_neighbours(row, col):
                    visited.add(p)
                    q.append(p)
                                    
            current_distance+=1 # update the level or distance from source
        
        return -1                