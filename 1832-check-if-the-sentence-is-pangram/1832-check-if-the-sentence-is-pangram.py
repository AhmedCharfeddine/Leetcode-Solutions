class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        uc = set()
        for i in sentence:
            uc.add(i)
        return len(uc) == 26