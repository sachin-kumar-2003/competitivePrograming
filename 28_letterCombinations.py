'''
Given a string containing digits from 2-9 inclusive,return all possible
letter combinations that the number could represent. 
A mapping of digits to letters (just like on the telephone buttons)
is given below. Note that 1 does not map to any letters.
Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]'''
from typing import List
class Solution:
  def letterCombinations(self, digits: str) -> List[str]:
    if digits=='':return []
    def backtrack(strg,idx):
      if len(strg)==len(digits):
        ans.append(strg)
        return
      num=int(digits[idx])
      for i in keyboard[num]:
        backtrack(strg+str(i),idx+1)
    keyboard=['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
    ans=[]
    backtrack('',0)
    return ans