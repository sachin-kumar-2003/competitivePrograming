''' Time Complexity O(N)
Maximum Ascending Subarray Sum
Given an array of positive integers nums, return the maximum
possible sum of an ascending subarray in nums.
A subarray is defined as a contiguous sequence of numbers in an array.
A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if
for all i where l <= i < r, numsi  < numsi+1. Note that a subarray
of size 1 is ascending.
Example 1:
Input: nums = [10,20,30,5,10,50]
Output: 65
Explanation: [5,10,50] is the ascending subarray with the maximum
sum of 65.
'''
from typing import List
class Solution:
  def maxAscendingSum(self, nums: List[int]) -> int:
    r=1
    ans=nums[0]
    curr=nums[0]
    while r<len(nums):
      if nums[r]>nums[r-1]:
        curr+=nums[r]
      else:
        curr=nums[r]
      ans=max(ans,curr)
      r+=1
    return ans