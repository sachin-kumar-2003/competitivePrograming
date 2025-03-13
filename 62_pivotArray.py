'''2161. Partition Array According to Given Pivot
The problem requires us to rearrange the array such that:
Elements smaller than the pivot appear first.
Elements equal to the pivot appear in the middle.
Elements greater than the pivot appear last.
The relative ordering of elements in each category is maintained.
Example:
Input: nums = [9,12,5,10,14,3,10], pivot = 10
Output: [9,5,3,10,10,12,14]

Here, 9, 5, 3 (smaller) come first, 10, 10 (equal) stay in the middle,
and 12, 14 (greater) come last, maintaining their relative order.
'''
from typing import List
class Solution:
  def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
    small,res,big=[],[],[]
    for num in nums:
      if num<pivot:
        small.append(num)
      elif num>pivot:
        big.append(num)
      else:
        res.append(num)
    return small+res+big