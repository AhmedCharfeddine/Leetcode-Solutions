class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = 0, len(matrix[0])-1
        while i<len(matrix) and j > -1:
            if matrix[i][j] == target:
                break
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return i < len(matrix) and j > -1