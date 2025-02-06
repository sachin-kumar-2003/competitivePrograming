'''Time Complexity O(N*N)
Given an array nums of distinct positive integers, return
the number of tuples (a, b, c, d) such that a * b = c * d
where a, b, c, and d are elements of nums, and a != b != c != d.
Example 1:
Input: nums = [2,3,4,6]
Output: 8
Explanation: There are 8 valid tuples:
(2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
(3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)'''
from collections import defaultdict
from typing import List
class Solution:
  def tupleSameProduct(self, nums: List[int]) -> int:
    product=defaultdict(int)
    ans=0
    for i in range(len(nums)):
      for j in range(i+1,len(nums)):
        product[nums[i]*nums[j]]+=1
    for key in product:
      if product[key]>=2:
        val=product[key]
        ans=ans+((val*(val-1))//2)*8
    return ans