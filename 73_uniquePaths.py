'''62. Unique Paths
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The test cases are generated so that the answer will be less than or equal to 2 * 109.
Input: m = 3, n = 7
Output: 28'''
from functools import lru_cache
class Solution:
  def uniquePaths(self, m: int, n: int) -> int:
    @lru_cache(None)
    def backtrack(i,j):
      if i==m-1 and j==n-1:
        return 1
      if i>=m or j>=n:
        return 0
      return backtrack(i+1,j)+backtrack(i,j+1)
    return backtrack(0,0)
        