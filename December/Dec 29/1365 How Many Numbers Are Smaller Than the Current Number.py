"""
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/

Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

"""

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        num = sorted(nums)
        hmap = {}
        ans = []
        for i in range(len(num)):
            if num[i] not in hmap:
                hmap[num[i]] = i
        for n in nums:
            ans.append(hmap[n])
        return ans


# More pythonic and faster solution

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        return [sorted(nums).index(i) for i in nums]
