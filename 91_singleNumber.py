'''136. Single Number'''
from typing import List
class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    num=nums[0]
    for i in range(1,len(nums)):
      num=nums[i]^num
    return num