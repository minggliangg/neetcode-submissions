# class BrowserHistory:
#     def __init__(self, homepage: str):
#         self.current_page = HistoryEntry(url=homepage)

#     def visit(self, url: str) -> None:
#         new_page = HistoryEntry(url=url, prev=self.current_page)
#         self.current_page.next = new_page
#         self.current_page = new_page

#     def back(self, steps: int) -> str:
        
#         for i in range(steps):
#             if self.current_page.prev is not None:
#                 self.current_page = self.current_page.prev
#             else: 
#                 break
#         return self.current_page.url

#     def forward(self, steps: int) -> str:

#         for i in range(steps):
#             if self.current_page.next is not None:
#                 self.current_page = self.current_page.next
#             else: 
#                 break
#         return self.current_page.url


# class HistoryEntry:
#     def __init__(self, url: str, next=None, prev=None):
#         self.url = url
#         self.next = next
#         self.prev = prev


# # Your BrowserHistory object will be instantiated and called as such:
# # obj = BrowserHistory(homepage)
# # obj.visit(url)
# # param_2 = obj.back(steps)
# # param_3 = obj.forward(steps)

class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.index = 0

    def visit(self, url: str) -> None:
        self.index += 1
        self.history[self.index:] = [url]  # replaces any forward history

    def back(self, steps: int) -> str:
        self.index = max(0, self.index - steps)
        return self.history[self.index]

    def forward(self, steps: int) -> str:
        self.index = min(len(self.history) - 1, self.index + steps)
        return self.history[self.index]