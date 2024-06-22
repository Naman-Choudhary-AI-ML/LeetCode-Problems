"""Problem:
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = []
        if root:
            stack.append((1, root))

        depth = 0
        while stack:
            curr_depth, root = stack.pop()
            if root:
                depth = max(depth, curr_depth)
                stack.append((curr_depth + 1, root.left))
                stack.append((curr_depth + 1, root.right))
        return depth