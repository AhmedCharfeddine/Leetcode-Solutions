class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # kadane's algorithm
        if len(nums) == 1:  return nums[0]
        
        def iterate_over(array):
            cur_prod = 1
            max_prod = -math.inf

            for i in array:
                if i == 0:  cur_prod = 1
                else:       
                    cur_prod *= i
                    max_prod = max(max_prod, cur_prod)
            return max_prod
            
        return max(iterate_over(nums), iterate_over(nums[::-1]), 0)