# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        new_head = None
        if list1 is None and list2 is not None:
            return list2

        if list2 is None and list1 is not None:
            return list1

        if list1 is None and list2 is None:
            return

        if list1.val <= list2.val:
            new_head = list1
            list1 = list1.next
        else:
            new_head = list2
            list2 = list2.next

        pointer = new_head

        while True:
            if list1 is None and list2 is not None:
                pointer.next = list2
                break
            if list2 is None and list1 is not None:
                pointer.next = list1
                break

            if list1 is None and list2 is None:
                break

            if list1.val <= list2.val:
                pointer.next = list1
                list1 = list1.next
            else:
                pointer.next = list2
                list2 = list2.next
            pointer = pointer.next
        return new_head
