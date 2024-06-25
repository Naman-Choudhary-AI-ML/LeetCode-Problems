"""Problem:
You are given a string s consisting only of lowercase English letters. We call a substring special if it contains no character which has occurred at least twice (in other words, it does not contain a repeating character). Your task is to count the number of special substrings. For example, in the string "pop", the substring "po" is a special substring, however, "pop" is not special (since 'p' has occurred twice).

Return the number of special substrings.

A substring is a contiguous sequence of characters within a string. For example, "abc" is a substring of "abcd", but "acd" is not.
"""

class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        start = 0
        count = 0
        track = {}
        for end in range(len(s)):
            if s[end] in track:
                track[s[end]] += 1
            else :
                track[s[end]] = 1
            
            while track[s[end]] > 1 :
                track[s[start]] -= 1
                if track[s[start]] == 0:
                    del track[s[start]]
                start += 1
            count += end - start + 1
        
        return count