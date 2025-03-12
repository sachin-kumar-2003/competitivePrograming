'''2460. Apply Operations to an Array
Given an array nums, perform n-1 operations:
If nums[i] == nums[i+1], double nums[i] and set nums[i+1] to 0.
Finally, shift all 0s to the end.
Example:
Input: nums = [1,2,2,1,1,0]
Output: [1,4,2,0,0,0]
Steps:
nums[1] == nums[2] → nums[1] *= 2, nums[2] = 0 → [1,4,0,1,1,0]
nums[3] == nums[4] → nums[3] *= 2, nums[4] = 0 → [1,4,0,2,0,0]
Shift zeros → [1,4,2,0,0,0]'''
from typing import List
class Solution:
  def applyOperations(self, nums: List[int]) -> List[int]:
    res=[0]*len(nums)
    idx=0
    for i in range(len(nums)-1):
      if nums[i]==nums[i+1]:
        nums[i]=nums[i]*2
        nums[i+1]=0
    for num in nums:
      if num != 0:
        res[idx]=num
        idx+=1
    return res