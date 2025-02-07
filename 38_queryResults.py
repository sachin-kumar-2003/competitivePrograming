''' Find the Number of Distinct Colors Among the Balls
You are given an integer limit and a 2D array queries of size n x 2.
There are limit + 1 balls with distinct labels in the range [0, limit].
Initially, all balls are uncolored. For every query in queries that is of the
form [x, y], you mark ball x with the color y. After each query, you need to
find the number of distinct colors among the balls.
Return an array result of length n, where result[i] denotes the number of distinct
colors after ith query.
Note that when answering a query, lack of a color will not be considered as a color.
Example 1:
Input: limit = 4, queries = [[1,4],[2,5],[1,3],[3,4]]
Output: [1,2,2,3]'''
from typing import List
import collections
class Solution:
  def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
    colored = {} 
    colorCount = collections.defaultdict(int)  
    ans = []
    for i, j in queries:
      if i in colored:
        prevColor = colored[i]
        colorCount[prevColor] -= 1
        if colorCount[prevColor] == 0:
          del colorCount[prevColor]  
      colored[i] = j
      colorCount[j] += 1  
      ans.append(len(colorCount))
    return ans