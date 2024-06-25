"""Problem:
Given an array of integer arrays arrays where each arrays[i] is sorted in strictly increasing order, return an integer array representing the longest common subsequence among all the arrays.

A subsequence is a sequence that can be derived from another sequence by deleting some elements (possibly none) without changing the order of the remaining elements.
"""
class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        if arrays:
            new = set(arrays[0])
        else:
            new = set()
        for x in range(len(arrays)):
            if x == 0:
                continue
            else :
                new = new & set(arrays[x])
        ans = list(new)
        ans.sort()
        return ans  

