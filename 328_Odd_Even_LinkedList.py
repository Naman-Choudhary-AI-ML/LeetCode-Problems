"""Problem:
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity."""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None :
            return None
        odd = head
        eve = head.next
        evestart = eve

        # count = 0
        # itr = head

        # while itr:
        #     itr = itr.next
        #     count += 1
        # length = count

        while eve and eve.next :
            odd.next = eve.next
            odd = odd.next
            eve.next = odd.next
            eve = eve.next
        odd.next = evestart

        return head