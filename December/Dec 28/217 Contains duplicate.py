"""
https://leetcode.com/problems/contains-duplicate/description/
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hmap = {}
        for i in range(len(nums)):
            if nums[i] not in hmap:
                hmap[nums[i]] = 1
            else:
                hmap[nums[i]] += 1
        return len(hmap.values()) != len(nums)
