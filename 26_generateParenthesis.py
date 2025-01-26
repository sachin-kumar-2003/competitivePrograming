'''Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]'''
from typing import List
class Solution:
  def generateParenthesis(self, n: int) -> List[str]:
    def backtracking(n,res,openP,closeP,currS):
      if openP==closeP and openP==n:
        res.append(currS)
        return
      if openP<n:backtracking(n,res,openP+1,closeP,currS+'(')
      if closeP<openP:backtracking(n,res,openP,closeP+1,currS+')')
    res=[]
    openP=0
    closeP=0
    backtracking(n,res,openP,closeP,'')
    return res
