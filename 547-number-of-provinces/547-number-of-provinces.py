class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        provinces = [0] * n
        provinces_count = 1
        
        def dfs(i, province):
            provinces[i] = province
            for j in range(n):
                if isConnected[i][j] and provinces[j] == 0:
                    dfs(j, province) 
        
        for i in range(n):
            if provinces[i] == 0:
                provinces[i] = provinces_count
                for j in range(i+1, n):
                    if isConnected[i][j]:
                        dfs(j, provinces_count)
                provinces_count += 1
        
        return provinces_count - 1