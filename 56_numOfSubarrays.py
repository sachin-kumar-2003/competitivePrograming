'''1524. Number of Sub-arrays With Odd Sum
Given an array of integers arr, return the number of subarrays with an odd sum.
Since the answer can be very large, return it modulo 109 + 7.
Example 1:
Input: arr = [1,3,5]
Output: 4
Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
All sub-arrays sum are [1,4,9,3,8,5].
Odd sums are [1,9,3,5] so the answer is 4.'''
from typing import List
class Solution:
  def numOfSubarrays(self, arr: List[int]) -> int:
    ans=prefix=oddCount=0
    evenCount,mod=1,10**9+7
    for num in arr:
      prefix+=num 
      if prefix%2==0:
        ans+=oddCount
        evenCount+=1
      else:
        ans+=evenCount
        oddCount+=1
    return ans%mod