class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i1, i2 = 0, 0
        d = {}
        n1, n2 = len(nums1), len(nums2)
        res = []
        while (i1 < n1):
            if nums1[i1] in d:
                d[nums1[i1]] += 1
            else:
                d[nums1[i1]] = 1
            i1 += 1
        while (i2 < n2):
            if nums2[i2] in d and d[nums2[i2]]>0:
                res.append(nums2[i2])
                d[nums2[i2]] -= 1
            i2 += 1
        return res