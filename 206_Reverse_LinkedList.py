"""Problem:
Given the head of a singly linked list, reverse the list, and return the reversed list."""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        itr = head
        while itr:
            nxt = itr.next
            itr.next = prev
            prev = itr
            itr = nxt

        head = prev
        return head



            



                        



        