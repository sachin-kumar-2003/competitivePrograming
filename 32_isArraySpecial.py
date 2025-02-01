'''
Special Array I
An array is considered special if every pair of its adjacent elements contains two
numbers with different parity.
You are given an array of integers nums. Return true if nums is a special array,
otherwise, return false.
Example 1:
Input: nums = [2,1,4]
Output: true
Explanation:
There is only two pairs: (2,1) and (1,4), and both of them contain numbers with
different parity. So the answer is true.
'''
from typing import List
class Solution:
  def isArraySpecial(self, nums: List[int]) -> bool:
    if len(nums)==1:return True
    for i in range(len(nums)-1):
      if nums[i]%2==0 and nums[i+1]%2==0 or nums[i]%2==1 and nums[i+1]%2==1:
        return False
    return True     