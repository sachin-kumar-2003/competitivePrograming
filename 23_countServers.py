'''Time Complexity O(N*M)
you are given a map of a server center, represented as a m * n integer
matrix grid, where 1 means that on that cell there is a server and 0 means
that it is no server. Two servers are said to communicate if they are on
the same row or on the same column.
Return the number of servers that communicate with any other server.
Example 1:
Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.'''
from typing import List
class Solution:
  def countServers(self, grid: List[List[int]]) -> int:
    ans=0
    row=[0]*len(grid[0])
    col=[0]*len(grid)
    for i in range(len(grid)):
      for j in range(len(grid[i])):
        if grid[i][j]==1:
          row[j]+=1
          col[i]+=1
    for i in range(len(grid)):
      for j in range(len(grid[i])):
        if grid[i][j]==1 and (row[j]>1 or col[i]>1):
          ans+=1
    return ans