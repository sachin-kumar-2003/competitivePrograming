'''1980. Find Unique Binary String
Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.
Example 1:
Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.'''
from typing import List
class Solution:
  def findDifferentBinaryString(self, nums: List[str]) -> str:
    def backtrack(idx,strg):
      if idx==len(nums):
        temp= ''.join(strg)
        if temp  not in nums:
          return temp
        return None
      first=backtrack(idx+1,strg)
      if first:return first
      strg[idx]='1'
      second=backtrack(idx+1,strg)
      if second:return second
      return None
    return backtrack(0,['0']*len(nums))