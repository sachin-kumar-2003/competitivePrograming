'''3208. Alternating Groups II
There is a circle of red and blue tiles. You are given an array of integers colors and an integer k. The color of tile i is represented by colors[i]:
colors[i] == 0 means that tile i is red.
colors[i] == 1 means that tile i is blue.
An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in the group except the first and last one has a different color from its left and right tiles).
Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.
Example 1:
Input: colors = [0,1,0,1,0], k = 3
Output: 3
'''
from typing import List
class Solution:
  def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
    size=len(colors)
    alter=1
    ans=0
    for i in range(size+k-1-1):
      if colors[i%size]==colors[(i-1)%size]:
        alter=1
      else:
        alter+=1
      if alter>=k:
        ans+=1
    return ans