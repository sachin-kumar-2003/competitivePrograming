'''3502.Minimum Cost to Reach Every Position
You are given an integer array cost of size n. You are currently at position n (at the end of the line) in a line of n + 1 people (numbered from 0 to n).
You wish to move forward in the line, but each person in front of you charges a specific amount to swap places. The cost to swap with person i is given by cost[i].
Note: Please do not copy the description during the contest to maintain the integrity of your submissions.
Example 1:
Input: cost = [5,3,4,1,3,2]
Output: [5,3,3,1,1,1]'''
from typing import List
class Solution:
  def minCosts(self, cost: List[int]) -> List[int]:
    for i in range(1,len(cost)):
      if cost[i]>cost[i-1]:
        cost[i]=cost[i-1]
    return cost