'''Time Complexity O(N)
Given a string s, return the number of unique palindromes of length three that are a subsequence of s.
Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.
A palindrome is a string that reads the same forwards and backwards.
A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
For example, "ace" is a subsequence of "abcde".
Example 1:

Input: s = "aabca"
Output: 3
Explanation: The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "aabca")
- "aaa" (subsequence of "aabca")
- "aca" (subsequence of "aabca")
'''
class Solution:
  def countPalindromicSubsequence(self, s: str) -> int:
    unique = set(s)
    pos = {}
    ans = 0
    for i in range(len(s)):
      if s[i] not in pos:
        pos[s[i]] = [i, i]
      else:
        pos[s[i]][1] = i
    for ch in pos.values():
      if ch[0] + 1 < ch[1]:
        tempStr = s[ch[0] + 1 : ch[1]]
        tempSet = set(tempStr)
        ans += len(tempSet)
    return ans
