"""
https://leetcode.com/problems/unique-number-of-occurrences/description/

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
"""

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hmap = {}

        for i in range(len(arr)):
            if arr[i] in hmap:
                hmap[arr[i]] += 1
            else:
                hmap[arr[i]] = 1
        return len(hmap) == len(set(hmap.values()))
