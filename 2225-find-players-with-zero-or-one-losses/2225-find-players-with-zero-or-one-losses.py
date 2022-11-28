class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        res0, res1, rest = set(), set(), set()
        for match in matches:
            winner, loser = match[0], match[1]
            if winner not in rest:
                if winner not in res1:
                    res0.add(winner)
            if loser not in rest:
                if loser not in res1:
                    if loser in res0:
                        res0.remove(loser)
                    res1.add(loser)
                else:
                    res1.remove(loser)
                    rest.add(loser)
        return [sorted(list(res0)), sorted(list(res1))]