class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:  return True
        closest_finish = len(nums) - 1
        for i in range(len((nums))-2, -1, -1):
            reach = i + nums[i]
            if reach >= closest_finish:  
                closest_finish = i
        return True if closest_finish == 0 else False