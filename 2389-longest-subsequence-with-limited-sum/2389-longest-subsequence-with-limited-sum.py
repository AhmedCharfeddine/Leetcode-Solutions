class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        if len(nums) == 1:  return [int(i>=nums[0]) for i in queries]
        nums.sort()
        cum_sum = [nums[0]]
        for i in range(1, len(nums)):
            cum_sum.append(cum_sum[-1]+nums[i])
        
        answer = []
        for query in queries:
            l = len(answer)
            for i in range(len(cum_sum)):
                if cum_sum[i] > query:
                    answer.append(i)
                    break
            # special case; the full array can be used as a subsequence
            if len(answer) == l:
                answer.append(len(cum_sum))
        return answer