class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, zeros, positives, negatives = set(), [], [], []
        for i in nums:
            if i < 0:   negatives.append(i)
            elif i == 0:    zeros.append(i)
            else:       positives.append(i)
        
        if len(zeros) >= 3:
            res.add((0,0,0))

        N, P = set(negatives), set(positives)
            
        if zeros:
            for p in positives:
                if -p in N:
                    res.add((-p, 0, p))
        
        if len(positives) > 1:
            for i in range(len(positives)-1):
                for j in range(i+1, len(positives)):
                    if -(positives[i]+positives[j]) in N:
                        res.add(tuple(sorted([-(positives[i]+positives[j]), positives[i], positives[j]])))
        
        if len(negatives) > 1:
            for i in range(len(negatives)-1):
                for j in range(i+1, len(negatives)):
                    if -(negatives[i]+negatives[j]) in P:
                        res.add(tuple(sorted([-(negatives[i]+negatives[j]), negatives[i], negatives[j]])))
                        
        return res