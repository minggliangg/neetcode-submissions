# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case
        if head is None or head.next is None:
            return head

        # Reverse everything after the current node
        new_head = self.reverseList(head.next)

        # Put the current node after its next node
        head.next.next = head

        # Remove the old forward link
        head.next = None

        return new_head