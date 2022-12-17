class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for char in tokens:
            try:
                stack.append(float(char))
            except ValueError:
                if char == '+':   op = float.__add__
                elif char == '-':   op = float.__sub__
                elif char == '*':   op = float.__mul__
                else:   op = lambda x,y: float(int(x / y))
                op2 = stack.pop()
                stack.append(op(stack.pop(), op2))
        return int(stack[0])