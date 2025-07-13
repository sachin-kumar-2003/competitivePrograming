'''213. House Robber II
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.'''
from typing import List
class Solution:
  def rob(self, nums: List[int]) -> int:
    if not nums:return 0
    if len(nums)==1:return nums[0]
    if len(nums)==2:return max(nums[0],nums[1])

    def rec(idx,nums,n,dp):
      if idx>n:return 0
      if dp[idx]!=-1:
        return dp[idx]
      dp[idx]=max(nums[idx]+rec(idx+2,nums,n,dp),rec(idx+1,nums,n,dp))
      return dp[idx]

    dp1=[-1]*(len(nums)+1)
    dp2=[-1]*(len(nums)+1)
    
    return max(rec(0,nums,len(nums)-2,dp1),rec(1,nums,len(nums)-1,dp2))