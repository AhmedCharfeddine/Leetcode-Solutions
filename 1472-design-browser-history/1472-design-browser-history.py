class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.cur_page = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.cur_page+1]
        self.history.append(url)
        self.cur_page += 1

    def back(self, steps: int) -> str:
        self.cur_page = max(self.cur_page - steps, 0)
        return self.history[self.cur_page]

    def forward(self, steps: int) -> str:
        self.cur_page = min(self.cur_page + steps, len(self.history) - 1)
        return self.history[self.cur_page]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)