class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:  return False
        remaining = sorted(list(set(hand)))
        count = Counter(hand)
        
        while remaining:
            v = remaining[0]
            count[v] -= 1
            if count[v] == 0:
                del count[v]
                remaining.pop(0)
            for i in range(1, groupSize):
                if not remaining or v+i not in count:
                    return False
                count[v+i] -= 1
                if count[v+i] == 0:
                    del count[v+i]
                    remaining.pop(0)
        
        return True