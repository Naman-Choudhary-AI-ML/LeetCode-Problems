"""Problem:
In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list."""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        ##Reversing second half of the linked list solution
        slow = head
        fast = head

        while fast:
            slow = slow.next
            fast = fast.next.next

        nxt = None
        prev = None

        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        start = head
        maxSum = 0

        while prev :
            maxSum = max(maxSum, start.val + prev.val)
            start = start.next
            prev = prev.next
        return maxSum


        """The first solution that came to my mind, using a list to store first half of linked list,
        and then adding the corresponding elements of the second half to elements in this list, 
        and finally finding maximum of the list"""
        # store = []
        # itr = head
        # count = 0
        # while itr:
        #     itr = itr.next
        #     count += 1
        # length = count

        # count = 0
        # itr = head
        # while itr :
        #     if count < length // 2 :
        #         store.append(itr.val)
        #     else :
        #         store[length - count - 1] += itr.val
        #     itr = itr.next
        #     count += 1
        # return max(store)