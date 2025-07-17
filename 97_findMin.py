'''153. Find Minimum in Rotated Sorted Array
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.'''
from typing import List
class Solution:
  def findMin(self, nums: List[int]) -> int:
    start=0
    end=len(nums)-1
    ans=nums[0]
    if len(nums)==1:return nums[0]
    while start<=end:
      if(nums[start]<=nums[end]):
        ans=min(ans,nums[start])
      mid=start+(end-start)//2
      ans=min(ans,nums[mid])
      if nums[start]<=nums[mid]:
        start=mid+1
      else:
        end=mid-1
    return ans