class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        visited = {tuple(entrance)}
        m, n = len(maze), len(maze[0])
        offsets = {(-1,0), (1,0), (0,1), (0,-1)}
        def get_neighbors(x, y):
            res = []
            for i,j in offsets:
                x_new = x + i
                y_new = y + j
                if 0 <= x_new < m and 0 <= y_new < n and maze[x_new][y_new] == '.' and (x_new,y_new) not in visited:
                    res.append((x_new,y_new))
            return res

        steps = 0
        queue = deque([tuple(entrance)])
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                if (x in [0, m-1] or y in [0, n-1]) and [x,y] != entrance:
                    return steps
                for x_new,y_new in get_neighbors(x, y):
                    visited.add((x_new,y_new))
                    queue.append((x_new,y_new))
            steps += 1
        return -1