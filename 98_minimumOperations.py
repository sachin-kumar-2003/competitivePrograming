'''3396. Minimum Number of Operations to Make Elements in Array Distinct
You are given an integer array nums. You need to ensure that the elements in the array are distinct. To achieve this, you can perform the following operation any number of times:
Remove 3 elements from the beginning of the array. If the array has fewer than 3 elements, remove all remaining elements.
Example 1:
Input: nums = [1,2,3,4,2,3,3,5,7]
Output: 2'''
from typing import List
from collections import Counter
class Solution:
  def minimumOperations(self, nums: List[int]) -> int:
    count=0
    freq=Counter(nums)
    def alldistinct(freq):
      for key in freq:
        if freq[key]>1:return False
      return True
    if alldistinct(freq):return count
    while len(nums)>=3:
      if alldistinct(freq):return count
      else:
        count+=1
        first,second,third=nums[0],nums[1],nums[2]
        freq[first]-=1
        freq[second]-=1
        freq[third]-=1
        nums=nums[3:]
    if alldistinct(freq):return count
    else:return count+1