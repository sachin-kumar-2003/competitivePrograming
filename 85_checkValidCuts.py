'''3394. Check if Grid can be Cut into Sections
You are given an integer n representing the dimensions of an n x n grid, with the origin at the bottom-left corner of the grid. You are also given a 2D array of coordinates rectangles, where rectangles[i] is in the form [startx, starty, endx, endy], representing a rectangle on the grid. Each rectangle is defined as follows:
(startx, starty): The bottom-left corner of the rectangle.
(endx, endy): The top-right corner of the rectangle.
Example 1:
Input: n = 5, rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]
Output: true'''
from collections import List
class Solution:
  def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
    x,y=[],[]
    for i in rectangles:
      x.append([i[0],i[2]])
      y.append([i[1],i[3]])
    x.sort()
    y.sort()
    def check(intervals):
      count=0
      prevEnd=-1
      for start,end in intervals:
        if prevEnd<=start:
          count+=1
        prevEnd=max(prevEnd,end)
      return count
    return max(check(x),check(y))>=3       