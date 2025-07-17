'''199. Binary Tree Right Side View
Given the root of a binary tree, imagine yourself standing on the
right side of it, return the values of the nodes you can see ordered
from top to bottom.
Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]'''
from typing import Optional,List
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class Solution:
  def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    maxLevel=[-1]
    ans=[]
    def dfs(node,curr):
      if node is None:
        return 
      if curr>maxLevel[0]:
        ans.append(node.val)
        maxLevel[0]=curr
      dfs(node.right,curr+1)
      dfs(node.left,curr+1)
    dfs(root,0)
    return ans