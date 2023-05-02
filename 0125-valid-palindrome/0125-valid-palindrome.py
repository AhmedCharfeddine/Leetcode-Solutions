class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = []
        for char in s:
            if char.isalnum():  clean.append(char.lower())
        return clean == clean[::-1]