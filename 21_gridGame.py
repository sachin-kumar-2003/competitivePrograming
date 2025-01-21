''' Time Complexity=O(N)
you are given a 0-indexed 2D array grid of size 2 x n, where grid[r][c] represents the number
of points at position (r, c) on the matrix. Two robots are playing a game on this matrix.
Both robots initially start at (0, 0) and want to reach (1, n-1). Each robot may only move to
the right ((r, c) to (r, c + 1)) or down ((r, c) to (r + 1, c)).
At the start of the game, the first robot moves from (0, 0) to (1, n-1), collecting all the
points from the cells on its path. For all cells (r, c) traversed on the path, grid[r][c]
is set to 0. Then, the second robot moves from (0, 0) to (1, n-1), collecting the points on
its path. Note that their paths may intersect with one another.
The first robot wants to minimize the number of points collected by the second robot. In contrast,
the second robot wants to maximize the number of points it collects. If both robots play optimally,
return the number of points collected by the second robot.
Input: grid = [[2,5,4],[1,5,1]]
Output: 4
Explanation: The optimal path taken by the first robot is shown in red, and the optimal path taken
by the second robot is shown in blue.
The cells visited by the first robot are set to 0.
The second robot will collect 0 + 0 + 4 + 0 = 4 points.'''
from typing import List
class Solution:
  def gridGame(self, grid: List[List[int]]) -> int:
    firstRow=0
    secondRow=0
    ans=float('inf')
    for i in grid[0]:
      firstRow+=i
    for i in range(len(grid[0])):
      firstRow-=grid[0][i]
      ans=min(ans,max(firstRow,secondRow))
      secondRow+=grid[1][i]
    return ans