'''
Check if Array Is Sorted and Rotated
Given an array nums, return true if the array was originally sorted
in non-decreasing order, then rotated some number of positions (including zero).
Otherwise, return false.
There may be duplicates in the original array.
Note: An array A rotated by x positions results in an array B of the same
length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.
Example 1:
Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 3 positions to begin on the the element of
value 3: [3,4,5,1,2].'''
from typing import List
class Solution:
  def check(self, nums: List[int]) -> bool:
    pivot=-1
    B=[]
    for i in range(len(nums)-1):
      if nums[i]>nums[i+1]:
        pivot=i
    if pivot==-1:return True
    for i in range(pivot+1,len(nums)):
      B.append(nums[i])
    for i in range(pivot+1):
      B.append(nums[i])
    for i in range(len(B)-1):
      if B[i]>B[i+1]:
        return False
    return True