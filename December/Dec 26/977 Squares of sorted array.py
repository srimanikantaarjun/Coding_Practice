"""
https://leetcode.com/problems/squares-of-a-sorted-array/description/
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i, num in enumerate(nums):
            nums[i] = num**2
        nums.sort()
        return nums
