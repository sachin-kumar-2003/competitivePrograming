'''4. Median of Two Sorted Arrays
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.'''
from typing import List
class Solution:
  def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    arr=nums1+nums2
    arr.sort()
    print(arr)
    if len(arr)%2==0:
      return (arr[(len(arr)//2)]+arr[(len(arr)//2)-1])/2
    else:
      return arr[(len(arr)//2)]
  