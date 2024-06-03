class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        smallest = min(candidates)
        
        combination = []
        cur_sum = 0
        def dfs(i):
            nonlocal cur_sum
            if i == len(candidates) or target - cur_sum < smallest:
                return
                        
            if cur_sum + candidates[i] == target:
                res.append(combination.copy() + [candidates[i]])
            
            if cur_sum + candidates[i] < target:
                cur_sum += candidates[i]
                combination.append(candidates[i])

                dfs(i)
                
                cur_sum -= candidates[i]
                combination.pop()
                
                dfs(i+1)
        
        dfs(0)
        return res