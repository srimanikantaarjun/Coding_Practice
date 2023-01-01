"""
https://leetcode.com/problems/search-insert-position/description/
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r)//2
            ele = nums[mid]

            if ele == target:
                return mid
            elif ele < target:
                l = mid + 1
            elif ele > target:
                r = mid - 1
        return l
