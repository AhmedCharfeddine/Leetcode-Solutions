class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for i in s:
            if i not in mapping:
                stack.append(i)
            elif not stack:
                return False
            elif mapping[i] != stack.pop(-1):
                return False
        if stack:
            return False
        return True