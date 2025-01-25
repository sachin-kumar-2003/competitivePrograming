''' COMBINATIONS SUM III
Find all valid combinations of k numbers that sum up to n such that
the following conditions are true:
Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not
contain the same combination twice, and the combinations may be returned
in any order.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.'''
from typing import List
class Solution:
  def combinationSum3(self, k: int, n: int) -> List[List[int]]:
    ans=[]
    def backtrack(k,total,temp,count):
      if total==n and k==0:
        ans.append(temp[:])
        return
      if total>n or k == 0 :
        return 
      for i in range(count,10):
        temp.append(i)
        backtrack(k-1,total+i,temp,i+1)
        temp.pop()
    backtrack(k,0,[],1)
    return ans
