"""
https://leetcode.com/problems/remove-vowels-from-a-string/description/

Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.
"""

class Solution:
    def removeVowels(self, s: str) -> str:
        vow = ["a", "e", "i", "o", "u"]
        for char in s:
            if char in vow:
                s = s.replace(char, "")
        return s


# s.c. = O(n)
# t.c. = O(1)
