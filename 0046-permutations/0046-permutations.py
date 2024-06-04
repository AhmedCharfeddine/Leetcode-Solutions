class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(indices: set[int]):
            for cur_idx in list(indices):
                indices.remove(cur_idx)
                subset.append(nums[cur_idx])

                if not indices:
                    res.append(subset.copy())
                else:
                    dfs(indices)
                    
                subset.pop()
                indices.add(cur_idx)
            
        dfs(set(range(len(nums))))
        
        return res