class Solution:
    def say(self, s):
        if len(s) == 1:
            return '1' + s
        i = 1
        res = []
        c = 1
        while i < len(s):
            if s[i] == s[i-1]:
                c += 1
            else:
                res.append(str(c)+s[i-1])
                c = 1
            i += 1
        res.append(str(c)+s[-1])
        return ''.join(res)
    
    def countAndSay(self, n: int) -> str:
        if n == 1:  return '1'
        return self.say(self.countAndSay(n-1))