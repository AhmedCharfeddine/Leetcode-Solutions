class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if len(cost) == 1:  return 0 if cost[0] <= gas[0] else -1
        start = 0
        while start < len(cost):
            gas_tank = 0
            finished = True
            for i in range(start, start+len(cost)):
                index = i % len(cost)
                gas_tank += (gas[index] - cost[index])
                if gas_tank < 0:
                    end = (index + (i == start)) % len(cost)
                    finished = False
                    break
            if finished:
                return start
            if end < start:
                return -1
            start = end
        return -1