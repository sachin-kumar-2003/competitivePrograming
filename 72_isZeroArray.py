'''3355. Zero Array Transformation I
You are given an integer array nums of length n and a 2D array queries,
where queries[i] = [li, ri].
For each queries[i]:
Select a subset of indices within the range [li, ri] in nums.
Decrement the values at the selected indices by 1.
A Zero Array is an array where all elements are equal to 0.
Return true if it is possible to transform nums into a Zero Array after
processing all the queries sequentially, otherwise return false.
Example 1:
Input: nums = [1,0,1], queries = [[0,2]]
Output: true'''
from typing import List
class Solution:
  def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
    prefix=[0]*(len(nums)+1)
    for i in range(len(queries)):
      left,right=queries[i]
      prefix[left]+=1
      prefix[right+1]-=1
    total=0
    for i in range(len(prefix)):
      total+=prefix[i]
      prefix[i]=total
    for i in range(len(nums)):
      nums[i]-=prefix[i]
    if all(x<=0 for x in nums):return True
    return False