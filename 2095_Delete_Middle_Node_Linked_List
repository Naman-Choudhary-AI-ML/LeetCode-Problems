"""Problem:
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively."""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # itr = head
        # count = 0
        # while itr :
        #     itr = itr.next
        #     count += 1
        # itr = head
        # length = count
        # count = 0
        # if length == 1:
        #     head = None
        #     return head
        # while itr:
        #     if count == length // 2 - 1:
        #         itr.next = itr.next.next
        #         break
        #     itr = itr.next
        #     count += 1
        
        # return head

        # Optimum Solution
        if head.next == None :
            return None
        slow = head
        fast = head.next.next

        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return head
        
        
        