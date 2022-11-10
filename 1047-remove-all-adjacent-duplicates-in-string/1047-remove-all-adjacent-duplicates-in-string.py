class Solution:
    def removeDuplicates(self, s: str) -> str:
        if len(s) <= 1:  return s
        l = list(s)
        i = 0
        while i < len(l)-1:
            if l[i] == l[i+1]:
                l.pop(i)
                l.pop(i)
                i = max(0, i-1)
            else:
                i += 1
        return ''.join(l)