class Solution:
    _end = '_end_'
    
    def make_trie(self, *words):
        root = dict()
        for word in words:
            current_dict = root
            for letter in word:
                current_dict = current_dict.setdefault(letter, {})
            current_dict[self._end] = self._end
        return root

    def find_root(self, trie, derivative):
        if derivative[0] not in trie:   return derivative
        root = []
        current_dict = trie
        found_root = False
        for letter in derivative:
            if self._end in current_dict:
                found_root = True
                break
            elif letter not in current_dict:
                break
            else:
                root.append(letter)
                current_dict = current_dict[letter]
        return ''.join(root) if found_root else derivative
    
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        res = []
        words = sentence.split(' ')
        trie = self.make_trie(*dictionary)
        print(trie)
        for derivative in words:
            res.append(self.find_root(trie, derivative))
        return ' '.join(res)
            