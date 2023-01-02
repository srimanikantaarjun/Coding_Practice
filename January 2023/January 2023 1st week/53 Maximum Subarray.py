"""
https://leetcode.com/problems/maximum-subarray/description/?envType=study-plan&id=data-structure-i
Given an integer array nums, find the 
subarray with the largest sum, and return its sum.
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub

