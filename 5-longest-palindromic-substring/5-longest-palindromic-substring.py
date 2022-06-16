class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        res_len = 0
        
        for i in range(len(s)):
            # odd length
            left = right = i
            is_palindrome = True
            while left >= 0 and right <= len(s)-1 and is_palindrome:
                if s[left] != s[right]: 
                    is_palindrome = False
                elif (right - left + 1) > res_len:
                    res = s[left:right+1]
                    res_len = right - left + 1
                left -= 1
                right += 1
            
            # even length
            if i == len(s)-1:
                break
            left, right = i, i+1
            is_palindrome = True
            while left >= 0 and right <= len(s)-1 and is_palindrome:
                if s[left] != s[right]: 
                    is_palindrome = False
                elif (right - left + 1) > res_len:
                    res = s[left:right+1]
                    res_len = right - left + 1
                left -= 1
                right += 1
        return res