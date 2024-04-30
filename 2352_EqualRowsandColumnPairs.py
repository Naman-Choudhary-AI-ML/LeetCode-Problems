"""Problem 2352 : Equal Row and Column Pairs
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, array):
        node = self.root
        for num in array:
            if num not in node.children:
                node.children[num] = TrieNode()
            node = node.children[num]
        node.count += 1
    def search(self, array):
        node = self.root
        for num in array:
            if num not in node.children:
                return 0
            node = node.children[num]
        return node.count


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        thetree = Trie()

        for row in grid :
            thetree.insert(row)
        n = len(grid)
        ans = 0
        for i in range(n):
            col = [grid[c][i] for c in range(n)]
            ans += thetree.search(col)
        return ans