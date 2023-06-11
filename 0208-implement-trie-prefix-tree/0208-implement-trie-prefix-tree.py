class Trie:

    def __init__(self):
        self.tree = {}

    def insert(self, word: str) -> None:
        tree = self.tree
        for char in word:
            if char not in tree:
                tree[char] = {}
            tree = tree[char]
        tree[None] = {}
        

    def search(self, word: str) -> bool:
        tree = self.tree
        for char in word:
            if char not in tree:
                return False
            tree = tree[char]
        return None in tree

    def startsWith(self, prefix: str) -> bool:
        tree = self.tree
        for char in prefix:
            if char not in tree:
                return False
            tree = tree[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)