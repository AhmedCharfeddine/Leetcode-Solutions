class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        if counter.most_common(1)[0][1] > (len(s) + 1)/2:
            return ''
        res = [None] * len(s)
        index = 0
        for item, count in counter.most_common():
            for _ in range(count):
                res[index] = item
                index += 2
                if index >= len(s):
                    index = 1
                
        return ''.join(res)