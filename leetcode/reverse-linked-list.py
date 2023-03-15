# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:

            next = head.next              # Store the next node to point to
            # print("next",next)

            head.next = prev              # Point the current node at the previous node. On the first iter this will point to null
            # print("head.next",head.next)

            prev = head                   # Update prev node with current node

            head = next                   # Move the pointer to the next node in the list
            # print("newhead",head)

        return prev