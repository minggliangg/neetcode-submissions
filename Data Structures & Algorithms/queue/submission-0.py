class Deque:
    
    def __init__(self):
        self.array = []


    def isEmpty(self) -> bool:
        return len(self.array) == 0
        

    def append(self, value: int) -> None:
        self.array.append(value)
        

    def appendleft(self, value: int) -> None:
        self.array = [value]+self.array
        

    def pop(self) -> int:
        if len(self.array) == 0:
            return -1
        return self.array.pop()
        

    def popleft(self) -> int:
        if len(self.array) == 0:
            return -1
        to_return = self.array[0]
        if len(self.array) == 1:
            self.array = []
        else:
            self.array = self.array[1:]
        return to_return
        
