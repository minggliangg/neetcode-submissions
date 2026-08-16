class LinkedList:
    #     def __init__(self):
    #         self.head = None
    #         self.tail = None
    #         self.size = 0
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    #     def get(self, index: int) -> int:
    #         if index < 0 or index >= self.size:
    #             return -1

    #         current_node = self.head
    #         if index == 0:
    #             return self.head.val
    #         while index > 0:
    #             current_node = current_node.ref
    #             index -= 1
    #         return current_node.val

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        current_node = self.head

        while index > 0:
            current_node = current_node.ref
            index -= 1

        return current_node.val

    #     def insertHead(self, val: int) -> None:
    #         if self.head is None:
    #             self.head = LinkNode(val)
    #         else:
    #             new_node = LinkNode(val, self.head)
    #             self.head = new_node
    #         if self.tail is None:
    #             self.tail = self.head
    #         self.size += 1

    def insertHead(self, val: int) -> None:
        new_node = LinkNode(val, self.head)
        self.head = new_node

        if self.tail is None:
            self.tail = new_node

        self.size += 1

    #     def insertTail(self, val: int) -> None:
    #         if self.tail is None:
    #             self.tail = LinkNode(val)
    #         else:
    #             new_node = LinkNode(val)
    #             self.tail.ref = new_node
    #             self.tail = new_node
    #         if self.head is None:
    #             self.head = self.tail
    #         self.size += 1
    def insertTail(self, val: int) -> None:
        new_node = LinkNode(val)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.ref = new_node
            self.tail = new_node

        self.size += 1

    #     def remove(self, index: int) -> bool:
    #         if index < 0 or index >= self.size:
    #             return False

    #         if self.size == 1:
    #             self.head = None
    #             self.tail = None
    #             self.size = 0
    #             return True
    #         prev_node = None
    #         current_node = self.head
    #         if index == 0:
    #             self.head = self.head.ref
    #             self.size -= 1
    #             return True
    #         while index > 0:
    #             prev_node = current_node
    #             current_node = current_node.ref
    #             index -= 1

    #         if current_node.ref is None:
    #             prev_node.ref = None
    #             self.tail = prev_node
    #         else:
    #             prev_node.ref = current_node.ref
    #         self.size -= 1
    #         return True

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False

        if index == 0:
            self.head = self.head.ref
            self.size -= 1

            if self.size == 0:
                self.tail = None

            return True

        prev_node = None
        current_node = self.head

        while index > 0:
            prev_node = current_node
            current_node = current_node.ref
            index -= 1

        prev_node.ref = current_node.ref

        if current_node == self.tail:
            self.tail = prev_node

        self.size -= 1
        return True

    #     def getValues(self) -> List[int]:
    #         current_node = self.head
    #         result = []
    #         for i in range(self.size):
    #             result.append(current_node.val)
    #             current_node = current_node.ref
    #         return result
    def getValues(self) -> List[int]:
        current_node = self.head
        result = []

        for _ in range(self.size):
            result.append(current_node.val)
            current_node = current_node.ref

        return result


class LinkNode:
    def __init__(self, val, ref=None):
        self.val = val
        self.ref = ref
