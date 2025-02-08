'''
Symmetric Tree
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
Input: root = [1,2,2,3,4,4,3]
Output: true
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
class Solution:
  def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    if root == None:return False
    def recursion(leftNode,rightNode):
      if leftNode==None and rightNode==None:
        return True
      if leftNode==None or rightNode==None or leftNode.val != rightNode.val:
        return False
      return recursion(leftNode.left,rightNode.right) and recursion(leftNode.right,rightNode.left)
    return recursion(root.left,root.right)