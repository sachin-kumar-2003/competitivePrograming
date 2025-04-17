'''746. Min Cost Climbing Stairs
You are given an integer array cost where cost[i] is the cost
of ith step on a staircase. Once you pay the cost, you can either climb
one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.
Example 1:
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.'''
from functools import lru_cache
from typing import List
class Solution:
  def minCostClimbingStairs(self, cost: List[int]) -> int:
    @lru_cache(None)
    def backtrack(idx):
      if idx>=len(cost):
        return 0
      return cost[idx]+min(backtrack(idx+1),backtrack(idx+2))
    return min(backtrack(0),backtrack(1))