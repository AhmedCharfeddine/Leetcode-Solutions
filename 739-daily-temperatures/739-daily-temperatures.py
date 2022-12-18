class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, res = deque(), [0] * len(temperatures)
        for i, elt in enumerate(temperatures):
            while stack and elt > temperatures[stack[-1]]:
                old_idx = stack.pop()
                res[old_idx] = i - old_idx
            stack.append(i)
        return res