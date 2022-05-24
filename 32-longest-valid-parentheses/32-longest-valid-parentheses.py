class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        pairs = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                try:
                    start_idx = stack.pop(-1)
                except:
                    continue
                pairs.append([start_idx, i])
        
        print(pairs)
        i = len(pairs) - 2
        while (i >= 0):
            while pairs[i+1][0] < pairs[i][0]:
                pairs.pop(i)
                if i == len(pairs)-1:
                    break
            i -= 1
                
        i = 0
        while (i < len(pairs) - 1):
            if pairs[i][1] == pairs[i+1][0] - 1 :
                pairs[i+1][0] = pairs[i][0]
                pairs.pop(i)
                if i == len(pairs)-1:
                    break
            else:
                i += 1
        
        print(pairs)
        return max([t[1] - t[0] + 1 for t in pairs] + [0])