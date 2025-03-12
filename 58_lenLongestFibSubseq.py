'''873. Length of Longest Fibonacci Subsequence
A sequence x1, x2, ..., xn is Fibonacci-like if:
n >= 3
xi + xi+1 == xi+2 for all i + 2 <= n
Given a strictly increasing array arr of positive integers
forming a sequence, return the length of the longest
Fibonacci-like subsequence of arr. If one does not exist,
return 0.
Example 1:
Input: arr = [1,2,3,4,5,6,7,8]
Output: 5
Explanation: The longest subsequence that is fibonacci-like:
[1,2,3,5,8].'''
from typing import List
class Solution:
  def lenLongestFibSubseq(self, arr: List[int]) -> int:
    ans=0
    hashSet=set(arr)
    for i in range(len(arr)):
      for j in range(i+1,len(arr)):
        first,second=arr[i],arr[j]
        series=2
        while first+second in hashSet:
          series+=1
          total=first+second
          first,second=second,total
          ans=max(series,ans)
    return ans