'''Time Complexity O(M*N)
You are given a 0-indexed integer array arr, and an m x n integer matrix mat.
arr and mat both contain all the integers in the range [1, m * n].
Go through each index i in arr starting from index 0 and paint the cell in mat 
containing the integer arr[i].
Return the smallest index i at which either a row or a column will be completely 
painted in mat.
Input: arr = [1,3,4,2], mat = [[1,4],[2,3]]
Output: 2
Explanation: The moves are shown in order, and both the first row and second column
of the matrix become fully painted at arr[2].'''
from typing import List
class Solution:
  def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
    hashArr={}
    for i in range(len(mat)):
      for j in range(len(mat[i])):
        hashArr[mat[i][j]]=(i,j)
    row=[0]*len(mat[0])
    col=[0]*len(mat)
    for i in range(len(arr)):
      (r,c)=hashArr[arr[i]]
      row[c]+=1
      col[r]+=1
      if row[c]==len(mat) or col[r]==len(mat[0]):
        return i
    return -1