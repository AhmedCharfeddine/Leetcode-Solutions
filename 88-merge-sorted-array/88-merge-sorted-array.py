class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
            
        i1, i2 = 0, 0
        new_m = m
        while (i2 < n) and (i1 < new_m):
            if nums1[i1] <= nums2[i2]:
                i1 += 1
                continue
            else:
                nums1.pop(-1)
                nums1.insert(i1, nums2[i2])
                i2 += 1
                i1 += 1
                new_m += 1
                
        if i1 == new_m:
            for i in range(i1, len(nums1)):
                nums1[i] = nums2[i2]
                i2 += 1