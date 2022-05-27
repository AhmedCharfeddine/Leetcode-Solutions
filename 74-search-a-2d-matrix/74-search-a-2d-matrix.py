class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        def find_row(start, finish):
            if start == finish:
                if matrix[start][0] <= target <= matrix[start][-1]:
                    return matrix[start]
                return None
            
            if target < matrix[start][0] or target > matrix[finish][-1]:
                return None
            
            r = (finish + start) // 2
            
            if matrix[r][0] <= target <= matrix[r][-1]:
                return matrix[r]
            
            elif target < matrix[r][0]:
                return find_row(start, r-1)
            else:
                return find_row(r+1, finish)
            
            
        row = find_row(0, len(matrix) - 1)
        if row:
            return target in row