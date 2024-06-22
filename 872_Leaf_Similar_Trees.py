"""Problem
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leave_seq(self, root, seq):
        if root is None:
            return
        if root.left is None and root.right is None:
            seq.append(root.val)

        if root.left:
            self.leave_seq(root.left, seq)

        if root.right:
            self.leave_seq(root.right, seq)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        seq1 = []
        seq2 = []

        self.leave_seq(root1, seq1)
        self.leave_seq(root2, seq2)

        return seq1 == seq2
        