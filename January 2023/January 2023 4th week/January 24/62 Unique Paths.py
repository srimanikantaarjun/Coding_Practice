"""
https://leetcode.com/problems/unique-paths/
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mat = [[0 for i in range(n)] for i in range(m)]
        for i in range(0, m):
            mat[i][0] = 1
        for j in range(0, n):
            mat[0][j] = 1
        for row in range(1, m):
            for col in range(1, n):
                mat[row][col] = mat[row-1][col] + mat[row][col-1]
        return mat[m-1][n-1]
