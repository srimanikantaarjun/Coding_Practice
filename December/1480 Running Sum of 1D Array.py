# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].


def runningSum(nums):
    runningSum = []
    for i in range(len(nums)):
        runningSum.append(sum(nums[0:i+1]))
    return runningSum


# Takeaways: Try using "+=" instead of "sum" function. This saves time and will
# lead to using less space.
