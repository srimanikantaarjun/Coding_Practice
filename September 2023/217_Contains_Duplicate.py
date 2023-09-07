# https://leetcode.com/problems/contains-duplicate/

def containsDuplicate(nums):
  hset = set()
  for ele in nums:
    if ele in hset:
      return True
    else:
      hset.add(ele)
  return False
