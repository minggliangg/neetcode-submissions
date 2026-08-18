class LinkNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current_node = self.head
        for i in range(index):
            current_node = current_node.next
        return current_node.val

    def addAtHead(self, val: int) -> None:
        new_node = LinkNode(val=val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = LinkNode(val=val)
        if self.tail is None:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            current_node = self.head
            for i in range(index):
                current_node = current_node.next
            new_node = LinkNode(val=val, next=current_node, prev=current_node.prev)
            current_node.prev.next = new_node
            current_node.prev = new_node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if self.size == 1:
            self.head = None
            self.tail = None
        elif index == 0:
            self.head = self.head.next
            self.head.prev = None
        elif index == self.size - 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            current_node = self.head
            for i in range(index):
                current_node = current_node.next
            current_node.prev.next = current_node.next
            current_node.next.prev = current_node.prev
        self.size -= 1