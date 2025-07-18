'''2401. Longest Nice Subarray
You are given an array nums consisting of positive integers.
We call a subarray of nums nice if the bitwise AND of every pair
of elements that are in different positions in the subarray is equal to 0.
Return the length of the longest nice subarray.
A subarray is a contiguous part of an array.
Note that subarrays of length 1 are always considered nice.
Example 1:
Input: nums = [1,3,8,48,10]
Output: 3
Explanation: The longest nice subarray is [3,8,48]. This subarray
satisfies the conditions:
- 3 AND 8 = 0.
- 3 AND 48 = 0.
- 8 AND 48 = 0.
It can be proven that no longer nice subarray can be obtained,
so we return 3'''
from typing import List
class Solution:
  def longestNiceSubarray(self, nums: List[int]) -> int:
    ans=0
    usedBit=0
    left=0
    for right,val in enumerate(nums):
      while usedBit&val:
        usedBit=usedBit^nums[left]
        left+=1
      usedBit=usedBit|val
      ans=max(ans,right-left+1)
    return ans