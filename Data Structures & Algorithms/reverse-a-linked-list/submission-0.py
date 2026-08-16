# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# [1,2,3,4,5]

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if head.next is None:
            return head
        
        prev_node = None
        current_node = head
        next_node =head.next

        while next_node is not None:
            current_node.next = prev_node # [1 None]
            prev_node = current_node 
            current_node=next_node 
            next_node = current_node.next 
        current_node.next = prev_node

        return current_node
        



        
        