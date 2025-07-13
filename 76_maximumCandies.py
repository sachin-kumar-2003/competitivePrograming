'''2226. Maximum Candies Allocated to K Children
You are given a 0-indexed integer array candies, where each element
represents a pile of candies of size candies[i]. You can divide each pile
into multiple sub-piles but cannot merge two piles together.
You are also given an integer k, representing the number of children.
Your task is to distribute the candies such that each child gets the
same maximum number of candies from a single pile. Some piles may remain unused.
Return the maximum number of candies each child can get.
Example 1:
Input: candies = [5,8,6], k = 3
Output: 5
Explanation: We can divide candies[1] into 2 piles of size 5 and 3,
and candies[2] into 2 piles of size 5 and 1. We now have five piles of
candies of sizes 5, 5, 3, 5, and 1. We can allocate the 3 piles of size 5 to 3
children. It can be proven that each child cannot receive more than 5 candies.'''
from typing import List
class Solution:
  def maximumCandies(self, candies: List[int], k: int) -> int:
    if sum(candies)<k:return 0
    left,right,ans=1,sum(candies)//k,0
    while left<=right:
      mid=(left+right)//2
      total=0
      for i in candies:
        total+=i//mid
      if total>=k:
        ans=mid
        left=mid+1
      else:
        right=mid-1
    return ans
