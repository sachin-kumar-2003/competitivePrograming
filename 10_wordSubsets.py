'''
You are given two string arrays words1 and words2.
A string b is a subset of string a if every letter in b occurs in a including multiplicity.
For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.
Return an array of all the universal strings in words1. You may return the answer in any order.
Example 1:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]
'''
from typing import List
class Solution:
  def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
    ans=[]
    freqW2=[0]*26
    for i in words2:
      count=[0]*26
      for j in i:
        count[ord(j)-ord('a')]+=1
      for i in range(26):
        freqW2[i]=max(freqW2[i],count[i])
    for i in words1:
      count=[0]*26
      isUniversal=True
      for j in i:
        count[ord(j)-ord('a')]+=1
      for j in range(26):
        if(freqW2[j]>count[j]):
          isUniversal=False
          break
        if isUniversal:
            ans.append(i)
    return ans
