'''74. Search a 2D Matrix
You are given an m x n integer matrix matrix with the following two properties:
Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.
Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true'''
from typing import List
class Solution:
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    def binarySearch(left,right,row):
      left=0
      right=len(matrix[row])-1
      while left<=right:
        mid=(left+right)//2
        if matrix[row][mid]==target:
          return True
        if matrix[row][mid]>target:
          right=mid-1
        else:
          left=mid+1
      return False
    for i in range(len(matrix)):
      if binarySearch(0,0,i):return True
    return False       