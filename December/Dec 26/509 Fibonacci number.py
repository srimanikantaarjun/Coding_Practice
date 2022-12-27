"""
https://leetcode.com/problems/fibonacci-number/description/
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
such that each number is the sum of the two preceding ones, starting from 0 and 1.
"""

class Solution:
    def fib(self, n: int) -> int:
        memo = {0: 0, 1: 1}
        if n in memo:
            return memo[n]
        memo[n] = self.fib(n-2) + self.fib(n-1)
        return memo[n]
