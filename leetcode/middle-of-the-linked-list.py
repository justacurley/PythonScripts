# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Get the length of the linked list
        cnt = 0
        length = head
        while length:
            cnt+=1
            length = length.next

        temp = head
        mid = cnt//2
        # Iterate through the list by the length of the list / 2
        while mid != 0:
            temp = temp.next
            mid -= 1
        return temp