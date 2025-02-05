''' Time Complexity O(N)
You are given two strings s1 and s2 of equal length. A string swap is
an operation where you choose two indices in a string (not necessarily different)
and swap the characters at these indices.
Return true if it is possible to make both strings equal by performing at most
one string swap on exactly one of the strings. Otherwise, return false.
Example 1:
Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 
o make "bank".'''

class Solution:
  def areAlmostEqual(self, s1: str, s2: str) -> bool:
    store=[]
    for i in range(len(s1)):
      if s1[i]!=s2[i]:
        store.append(i)
      if len(store)>2:
        return False
    if len(store)==0:return True
    if len(store)==1:return False
    i,j=store
    if s1[i]==s2[j] and s1[j]==s2[i]:
        return True
    else:return False