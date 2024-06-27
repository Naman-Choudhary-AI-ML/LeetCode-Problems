"""Problem:
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0

        def preorder(node, curr_sum):
            nonlocal count
            if not node:
                return
            curr_sum += node.val
            if curr_sum == targetSum:
                count += 1

            count += h[curr_sum - targetSum]

            h[curr_sum] += 1

            preorder(node.left, curr_sum)
            preorder(node.right, curr_sum)

            h[curr_sum] -= 1
             
        h = defaultdict(int)
        preorder(root, 0)

        return count