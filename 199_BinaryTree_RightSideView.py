"""Problem:
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        if root:
            queue.append((root, 0))
        ans = []
        checkedlevels = defaultdict(int)
        print(queue)

        while len(queue) > 0:
            node, level = queue.popleft()
            if level not in checkedlevels:
                ans.append(node.val)
                checkedlevels[level] = 1
            if node.right:
                queue.append((node.right, level + 1))
            if node.left:
                queue.append((node.left, level + 1))
        return ans