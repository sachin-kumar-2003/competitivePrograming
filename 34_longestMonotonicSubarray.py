'''Longest Strictly Increasing or Strictly Decreasing Subarray
You are given an array of integers nums. Return the length of the longest 
subarray of nums which is either strictly increasing or strictly decreasing
Example 1:
Input: nums = [1,4,3,3,2]
Output: 2
Explanation:
The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].
The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2], and [4,3].
Hence, we return 2.'''
from typing import List
class Solution:
  def longestMonotonicSubarray(self, nums: List[int]) -> int:
    ans=1
    incrementing=1
    decrementing=1
    for i in range(len(nums)-1):
      if nums[i]<nums[i+1]:
        decrementing=1
        incrementing+=1
      elif nums[i]>nums[i+1]:
        incrementing=1
        decrementing+=1
      else:
        incrementing=1
        decrementing=1
      ans=max(ans,incrementing,decrementing)
    return ans