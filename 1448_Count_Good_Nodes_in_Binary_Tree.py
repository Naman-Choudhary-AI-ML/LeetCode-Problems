"""Problem
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None, maxi = None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:

    # Recursive Solution
    def good(self, root, count, maxi):
        if root.left is None and root.right is None :
            return count
        if root.left:
            max_new = max(maxi, root.left.val)
            if root.left.val >= maxi:
                count += 1
            count = self.good(root.left, count, max_new)
        if root.right:
            max_new = max(maxi, root.right.val)
            if root.right.val >= maxi :
                count += 1
            count = self.good(root.right, count, max_new)
        return count


    def goodNodes(self, root: TreeNode) -> int:
        count = self.good(root, 0, root.val)
        return count + 1

    #Iterative Solution using stack and DFS

    def goodNodes(self, root: TreeNode) -> int:
        stack = []
        stack.append((root, root.val))
        goodnodes = 0

        while stack:
            root, maxval = stack.pop()
            if root.val >= maxval :
                maxval = root.val
                goodnodes += 1
            if root.right:
                stack.append((root.right, maxval))
            if root.left:
                stack.append((root.left, maxval))
        return goodnodes

    #Iterative Solution using Queue and BFS

    def goodNodes(self, root: TreeNode) -> int:
        queue = deque()
        queue.append((root, root.val))
        count = 0

        while queue:
            node, maxval = queue.popleft()
            if node.val >= maxval :
                maxval = node.val
                count += 1
            if node.left:
                queue.append((node.left, maxval))
            if node.right:
                queue.append((node.right, maxval))
        return count