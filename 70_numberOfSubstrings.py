'''1358. Number of Substrings Containing All Three Characters
Given a string s consisting only of characters a, b and c.
Return the number of substrings containing at least one occurrence
of all these characters a, b and c.
Example 1:
Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least
one occurrence of the characters a, b and c are
"abc", "abca", "abcab", "abcabc", "bca", "bcab",
"bcabc", "cab", "cabc" and "abc" (again).'''
from collections import defaultdict
class Solution:
  def numberOfSubstrings(self, s: str) -> int:
    countABC=defaultdict(int)
    left=0
    ans=0
    for right in range(len(s)):
      if s[right] in 'abc':
        countABC[s[right]]+=1
      while len(countABC)==3:
        ans+=len(s)-right
        countABC[s[left]]-=1
        if countABC[s[left]]==0:
          countABC.pop(s[left])
        left+=1
    return ans