''' Time Complexity (2^N)
Given a string s, partition s such that every 
substring of the partition is a palindrome Return all possible
palindrome partitioning of s.
Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]'''
from typing import List
class Solution:
  def partition(self, s: str) -> List[List[str]]:
    ans=[]
    temp=[]
    def isPallindrome(s):
      start=0
      end=len(s)-1
      while start<end:
        if s[start]!=s[end]:return False
        start+=1
        end-=1
      return True          
    def backtrack(idx):
      if idx == len(s):
        ans.append(temp[:])
        return 
      for i in range(idx,len(s)):
        if isPallindrome(s[idx:i+1]):
          temp.append(s[idx:i+1])
          backtrack(i+1)
          temp.pop()     
    backtrack(0)
    return ans