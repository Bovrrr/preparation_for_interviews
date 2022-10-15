# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        prev_node = None
        curr_node = head
        next_node = head

        while next_node.next is not None:
            next_node = next_node.next
            curr_node.next = prev_node

            prev_node = curr_node
            curr_node = next_node

        curr_node.next = prev_node
        head = next_node
        return head
