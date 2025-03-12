'''150. Evaluate Reverse Polish Notation
You are given an array of strings tokens that represents
an arithmetic expression in a Reverse Polish Notation.
Evaluate the expression. Return an integer that represents
the value of the expression.
Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9'''
from typing import List
class Solution:
  def evalRPN(self, tokens: List[str]) -> int:
    stack=[]
    operators=['+','-','*','/']
    for ch in tokens:
      if ch in operators:
        first=stack.pop()
        second=stack.pop()
        if ch=='+':stack.append(first+second)
        if ch=='-':stack.append(second-first)
        if ch=='*':stack.append(second*first)
        if ch=='/':stack.append(int(second/first))
      else:
        stack.append(int(ch))
    return stack[0]