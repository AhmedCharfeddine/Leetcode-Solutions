class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s).most_common()  # count characters and sort them in reverse order
        return ''.join([char*freq for char,freq in counter])