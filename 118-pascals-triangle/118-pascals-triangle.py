class Solution:
    def generate(self, n: int) -> List[List[int]]:
        if n == 1:  return [[1]]
        elif n == 2:    return [[1], [1, 1]]
        
        res = [[1], [1, 1]]
        for i in range(2, n):
            new = [1]
            for j in range(1, i):
                new.append(res[-1][j] + res[-1][j-1])
            print(new)
            res.append(new + [1])
            
        return res