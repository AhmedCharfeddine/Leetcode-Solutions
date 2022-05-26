class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m,n = len(mat), len(mat[0])
        if m*n != r*c:
            return mat
        res = [[0 for _ in range(c)] for _ in range(r)]
        flattened = []
        print(res)
        for row in mat:
            for cell in row:
                flattened.append(cell)
        else:
            for i1 in range(r):
                for i2 in range(c):
                    res[i1][i2] = flattened[i1*c + i2]

        return res