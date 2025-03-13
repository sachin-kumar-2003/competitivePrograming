'''2570. Merge Two 2D Arrays by Summing Values
You are given two sorted 2D integer arrays, nums1 and nums2, where:
nums1[i] = [idi, vali] represents an element with id = idi and value = vali.
nums2[i] = [idi, vali] follows the same format.
Each array has unique ids and is already sorted in ascending order by id.
Your task is to merge the two arrays into a single sorted array, ensuring:
Only unique ids are included.
nums1 = [[1,2],[2,3],[4,5]]  
nums2 = [[1,4],[3,2],[4,1]]  
Output:[[1,6],[2,3],[3,2],[4,6]]'''
from typing import List
class Solution:
  def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
    res=[]
    i,j=0,0
    while i<len(nums1) and j<len(nums2):
      if nums1[i][0]==nums2[j][0]:
        res.append([nums1[i][0],nums1[i][1]+nums2[j][1]])
        i,j=i+1,j+1
      elif nums1[i][0]<nums2[j][0]:
        res.append([nums1[i][0],nums1[i][1]])
        i+=1
      else:
        res.append([nums2[j][0],nums2[j][1]])
        j+=1
    res.extend(nums1[i:])
    res.extend(nums2[j:])
    return res