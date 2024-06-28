"""Problem:
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        if root:
            queue.append((root, 1))
        levelsum = defaultdict(int)
        while queue:
            node, level = queue.popleft()
            levelsum[level] += node.val
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        maxsum = float('-inf')
        ans = 0
        return max(levelsum, key=levelsum.get)