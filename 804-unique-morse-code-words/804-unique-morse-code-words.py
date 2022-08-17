class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        unique = set()
        for word in words:
            transformation = []
            for char in word:
                transformation.append(morse[ord(char) - 97])
            unique.add(''.join(transformation))
        return len(unique)