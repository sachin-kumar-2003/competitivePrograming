'''Time Complexity O(N)
You are given two 0-indexed arrays, nums1 and nums2, consisting of non-negative 
integers. There exists another array, nums3, which contains the bitwise XOR of 
all pairings of integers between nums1 and nums2 (every integer in nums1 is paired
with every integer in nums2 exactly once).
Example 1:

Input: nums1 = [2,1,3], nums2 = [10,2,5,0]
Output: 13
Explanation:
A possible nums3 array is [8,0,7,2,11,3,4,1,9,1,6,3].
The bitwise XOR of all these numbers is 13, so we return 13.
'''
from typing import List
class Solution:
  def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
    ansXOR=0
    if len(nums1)%2==0 and len(nums2)%2==0:
      return 0
    else:
      for i in range(len(nums1)):
        if len(nums2)%2==1:ansXOR=ansXOR^nums1[i]
      for i in range(len(nums2)):
        if len(nums1)%2==1:ansXOR=ansXOR^nums2[i]
    return ansXOR  