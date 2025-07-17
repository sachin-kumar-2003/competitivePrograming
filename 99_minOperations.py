'''3375. Minimum Operations to Make Array Values Equal to K
You are given an integer array nums and an integer k.
An integer h is called valid if all values in the array that are strictly greater than h are identical.
For example, if nums = [10, 8, 10, 8], a valid integer is h = 9 because all nums[i] > 9 are equal to 10, but 5 is not a valid integer.
Example 1:
Input: nums = [5,2,5,4,5], k = 2
Output: 2
Explanation:
The operations can be performed in order using valid integers 4 and then 2.'''
from typing import List
class Solution:
  def minOperations(self, nums: List[int], k: int) -> int:
    if k>min(nums):return -1
    distinct=set(nums)
    distinctLength=len(distinct)
    if k in distinct:
      return distinctLength-1
    else:
      return distinctLength