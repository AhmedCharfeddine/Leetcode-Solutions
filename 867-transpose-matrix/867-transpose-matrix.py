class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        for i in range(len(matrix[0])):
            new_row = []
            for j in range(len(matrix)):
                new_row.append(matrix[j][i])
            res.append(new_row)
        return res