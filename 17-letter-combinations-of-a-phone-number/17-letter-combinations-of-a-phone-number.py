class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_map = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        def helper(digits):
            if len(digits) == 0:  return ['']
            res = []
            for i in phone_map[digits[0]]:
                for s in helper(digits[1:]):
                    res.append(i+s)
            return res
        
        if digits == "":    return []
        return helper(digits)
        