class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:  return False
        if k >= len(nums)-1:
            # base problem
            return len(set(nums)) != len(nums)
        
        window = {nums[i] for i in range(k)}
        
        for i in range(k, len(nums)):
            if nums[i] in window:
                return True
            window.add(nums[i])
            window.remove(nums[i-k])
        
        return False