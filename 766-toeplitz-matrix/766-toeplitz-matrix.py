class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        if 1 in {m, n}: return True
        
        # looping horizontally
        for j in range(n):
            i1, j1 = 0, j
            elt = matrix[i1][j1]
            while i1 < m and j1 < n:
                if matrix[i1][j1] != elt:   return False
                i1 += 1
                j1 += 1
            
        # looping vertically
        for i in range(m):
            i1, j1 = i, 0
            elt = matrix[i1][j1]
            while i1 < m and j1 < n:
                if matrix[i1][j1] != elt:   return False
                i1 += 1
                j1 += 1

        return True