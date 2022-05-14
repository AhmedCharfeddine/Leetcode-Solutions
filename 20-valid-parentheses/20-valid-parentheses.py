class Solution:
    def equivalent(self, char):
        if char == ')':
            return '('
        elif char == '}':
            return '{'
        elif char == ']':
            return '['
            
        return '0'
            
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        
        
            
        stack = []
        for char in s:
            if char in ['{', '[', '(']:
                stack.append(char)

            elif char in ['}', ']', ')']:
                if len(stack) == 0:
                    return False
                elif self.equivalent(char) != stack[-1]:
                    return False
                stack.pop(-1)

        if len(stack) == 0:
            return True
        return False