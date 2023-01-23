"""
https://leetcode.com/problems/climbing-stairs/description/
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        arr = [None, 1, 2, None]
        for i in range(3, n+1):
            arr[i%3] = arr[(i-1)%3] + arr[(i-2)%3]
        return arr[n%3]
