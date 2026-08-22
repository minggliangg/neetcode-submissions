class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self) -> bool:
        return self.head is None and self.tail is None

    def append(self, value: int) -> None:
        newElement = QueueElement(value=value, prev=self.tail)
        if self.head is None and self.tail is None:
            self.head = newElement
            self.tail = newElement

        else:
            self.tail.next = newElement
            self.tail = self.tail.next

    def appendleft(self, value: int) -> None:
        newElement = QueueElement(value=value)
        if self.head is None and self.tail is None:
            self.head = newElement
            self.tail = newElement
        else:
            self.head.prev = newElement
            newElement.next = self.head
            self.head = newElement

    def pop(self) -> int:
        if self.tail is None:
            return -1

        result = self.tail.value
        self.tail = self.tail.prev

        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None

        return result

    def popleft(self) -> int:
        if self.head is None:
            return -1
        result = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        return result


class QueueElement:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev
