'''875. Koko Eating Bananas'''
from collections import List
import math
class Solution:
  def minEatingSpeed(self, piles: List[int], h: int) -> int:
    ans=max(piles)
    left,right=1,max(piles)
    while left<=right:
      mid=(left+right)//2
      total=0
      for i in piles:
        total+=math.ceil(i/mid)
      if h>=total:
        ans=mid
        right=mid-1
      else:left=mid+1
    return ans