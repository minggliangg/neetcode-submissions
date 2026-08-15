class MinStack:
    def __init__(self):
        self.stack = []
        self.lowest_index = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if  not self.lowest_index or val < self.stack[self.lowest_index[-1]] :
            self.lowest_index.append(len(self.stack) - 1)

    def pop(self) -> None:
        if self.lowest_index[-1] == (len(self.stack) - 1):
            self.lowest_index.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:

        return self.stack[self.lowest_index[-1]]
