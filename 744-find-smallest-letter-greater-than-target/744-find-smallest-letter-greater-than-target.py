class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start, stop = 0, len(letters)-1
        if letters[start] > target or target > letters[stop]:
            return letters[start]
        while stop - start > 1:
            pos = math.ceil((start+stop)/2)
            if letters[pos] > target:
                stop = pos
            elif letters[pos] < target:
                start = pos
            else:
                while pos<len(letters) and letters[pos] == letters[(pos+1)%len(letters)]:
                    pos += 1
                return letters[(pos+1)%len(letters)]
        
        while stop<len(letters) and letters[stop] == letters[(stop+1)%len(letters)]:
            stop += 1
        if letters[stop] > target:
            return letters[stop]
        return letters[(stop+1)%len(letters)]