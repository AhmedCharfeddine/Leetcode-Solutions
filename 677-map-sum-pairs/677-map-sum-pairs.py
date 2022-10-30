class MapSum:

    def __init__(self):
        self.original_queries = {}
        self.d = {}

    def insert(self, key: str, val: int) -> None:
        old_val = self.original_queries.get(key, 0)
        for i in range(1, len(key)+1):
            s = key[:i]
            if s in self.d:
                self.d[s] += val - old_val
            else:
                self.d[s] = val
        self.original_queries[key] = val
        
    def sum(self, prefix: str) -> int:
        return self.d.get(prefix, 0)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)