class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sum_evens = sum([i for i in nums if i % 2 == 0])
        answer = []
        
        for val, index in queries:
            old_val = nums[index]
            if old_val % 2 == val % 2:
                sum_evens += val
                if old_val % 2 == 1:
                    sum_evens += old_val
            else:
                if old_val % 2 == 0:
                    sum_evens -= old_val
            nums[index] += val
            answer.append(sum_evens)
        
        return answer