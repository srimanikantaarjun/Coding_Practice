"""
https://leetcode.com/problems/single-row-keyboard/description/

There is a special keyboard with all keys in a single row.

Given a string keyboard of length 26 indicating the layout of the keyboard (indexed from 0 to 25).
Initially, your finger is at index 0. To type a character, you have to move your finger to the index of the desired character.
The time taken to move your finger from index i to index j is |i - j|.

You want to type a string word. Write a function to calculate how much time it takes to type it with one finger.
"""

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        hmap = {}
        cur = 0
        pre = 0
        tot = 0
        for i in range(len(keyboard)):
            hmap[keyboard[i]] = i
        for char in word:
            cur = pre
            pre = hmap[char]
            tot += abs(pre - cur)
        return tot
