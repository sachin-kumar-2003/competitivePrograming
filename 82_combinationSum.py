'''39. Combination Sum
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.'''
from collections import List
class Solution:
  def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    def backtracking(candidates,target,total,ans,tempArr,idx):
      if idx==len(candidates):return
      if total==target:
        ans.append(tempArr[:])
        return
      if total>target:
        return
      total+=candidates[idx]
      tempArr.append(candidates[idx])
      backtracking(candidates,target,total,ans,tempArr,idx)
      item=tempArr.pop()
      total-=item
      backtracking(candidates,target,total,ans,tempArr,idx+1)
    ans=[]
    tempArr=[]
    backtracking(candidates,target,0,ans,tempArr,0)
    return ans