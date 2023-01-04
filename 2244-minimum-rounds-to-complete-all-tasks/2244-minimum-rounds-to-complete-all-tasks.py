class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        res = 0
        for diff in Counter(tasks).values():
            if diff == 1:   return -1
            res += diff // 3 + int(diff % 3 != 0)
        return res