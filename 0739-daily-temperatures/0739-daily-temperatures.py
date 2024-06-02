class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, res = deque(), [0] * len(temperatures)
        for i in range(len(temperatures)):
            continue_condition = True
            while stack and continue_condition:
                last_pos = stack.pop()
                if temperatures[last_pos] < temperatures[i]:
                    res[last_pos] = i - last_pos
                else:
                    stack.append(last_pos)
                    continue_condition = False
            stack.append(i)
        return res            