"""
Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it into some number of substrings such that:

Each substring is balanced.
Return the maximum number of balanced strings you can obtain.

https://leetcode.com/problems/split-a-string-in-balanced-strings/

"""

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = cnt = 0         
        for c in s:
            if c == 'L':
                cnt += 1
            else:
                cnt -= 1            
            if cnt == 0:
                res += 1
        return res
