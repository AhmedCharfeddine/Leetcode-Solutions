class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        uc = set()
        for i in sentence:
            uc.add(i)
            if len(uc) == 26:
                return True
        return False