'''32. Longest Valid Parentheses
')', return the length of the longest valid (well-formed) parentheses 
substring.
Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".'''
class Solution:
  def longestValidParentheses(self, s: str) -> int:
    ans=open=close=0
    for c in s:
      if c=='(':open+=1
      else:close+=1
      if close>open:open=close=0
      if open==close:ans=max(ans,open+close)
    open=close=0
    for c in reversed(s):
      if c==')':close+=1
      else:open+=1
      if open>close:open=close=0
      if open==close:ans=max(ans,open+close)
    return ans