class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        
        for i in range(len(matrix)):
            matrix[i].insert(0, 0)
            for j in range(1, len(matrix[0])):
                self.matrix[i][j] += self.matrix[i][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        i = row1
        
        while i <= row2:
            res += self.matrix[i][col2+1] - self.matrix[i][col1]
            i += 1
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)