# https://leetcode.com/problems/build-array-from-permutation/

class Solution:
	def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums.append(nums[nums[i]])
        for i in range(len(nums)//2):
            nums.pop(0)
        return nums

