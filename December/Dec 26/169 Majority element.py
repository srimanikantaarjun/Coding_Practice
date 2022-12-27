"""
https://leetcode.com/problems/majority-element/description/
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hmap = {}
        for num in nums:
            if num not in hmap:
                hmap[num] = 1
            else:
                hmap[num] += 1
        for key, val in hmap.items():
            if val > len(nums)/2:
                return key
