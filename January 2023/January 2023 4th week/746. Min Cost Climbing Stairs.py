"""
https://leetcode.com/problems/min-cost-climbing-stairs/description/
You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        ans = [0] * (n+2)
        ans[0] = 0
        ans[1] = cost[0]
        cost.append(0)
        for i in range(2, n+2):
            ans[i] = cost[i-1] + min(ans[i-1], ans[i-2])
        return ans[n+1]
