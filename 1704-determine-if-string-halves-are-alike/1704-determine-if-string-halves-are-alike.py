class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        count = 0
        for i in range(len(s)):
            count += (-1)**(i < len(s)//2) * (s[i] in vowels)
        return not bool(count)