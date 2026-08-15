class DynamicArray:
    # def __init__(self, capacity: int):
    #     self.array = [None] * capacity
    #     self.size = 0
    #     self.capacity = capacity

    # def get(self, i: int) -> int:
    #     return self.array[i]

    # def set(self, i: int, n: int) -> None:
    #     self.array[i] = n

    # def pushback(self, n: int) -> None:
    #     if self.size == self.capacity:
    #         self.resize()

    #     self.array[self.size] = n
    #     self.size += 1

    # def popback(self) -> int:
    #     result = self.array[self.size - 1]
    #     self.array[self.size - 1] = None
    #     self.size -= 1
    #     return result

    # def resize(self) -> None:
    #     new_array = [None] * (2 * self.capacity)

    #     for i in range(self.size):
    #         new_array[i] = self.array[i]

    #     self.array = new_array
    #     self.capacity *= 2

    # def getSize(self) -> int:
    #     return self.size

    # def getCapacity(self) -> int:
    #     return self.capacity
    __slots__ = ("_array", "_size", "_capacity")

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._size = 0
        self._array = [None] * capacity

    def get(self, i: int) -> int:
        return self._array[i]

    def set(self, i: int, n: int) -> None:
        self._array[i] = n

    def pushback(self, n: int) -> None:
        if self._size == self._capacity:
            self.resize()
        self._array[self._size] = n
        self._size += 1

    def popback(self) -> int:
        self._size -= 1
        return self._array[self._size]

    def resize(self) -> None:
        self._array += [None] * self._capacity
        self._capacity *= 2

    def getSize(self) -> int:
        return self._size

    def getCapacity(self) -> int:
        return self._capacity