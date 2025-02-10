'''Time Complexity O(N)
You are given a string s.
Your task is to remove all digits by doing this operation repeatedly:
Delete the first digit and the closest non-digit character to its left.
Return the resulting string after removing all digits.
Example 1:
Input: s = "abc"
Output: "abc"
Explanation:
There is no digit in the string.'''
class Solution:
  def clearDigits(self, s: str) -> str:
    stack=[]
    for ch in s:
      if ch.isdigit():
        stack.pop()
      else:
        stack.append(ch)
    return "".join(stack)