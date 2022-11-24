class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        if len(word) > n*m: return False
        offsets = {(-1, 0), (1, 0), (0, 1), (0, -1)}
        visited = set()
        def helper(x, y, word):
            if board[x][y] != word[0]:  return False
            elif len(word) == 1:    return True
            if len(visited) == n*m-1:   return True
            visited.add((x,y))
            for x_offset, y_offset in offsets:
                x_new, y_new = x+x_offset, y+y_offset
                if 0 <= x_new < n and 0 <= y_new < m and (x_new,y_new) not in visited:
                    if helper(x_new, y_new, word[1:]):  return True
            visited.remove((x,y))
            return False
        
        for i in range(n):
            for j in range(m):
                if helper(i,j,word):    return True
        return False