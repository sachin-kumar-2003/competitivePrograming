'''69. Sqrt(x)
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.'''
class Solution:
  def mySqrt(self, x: int) -> int:
    if x==1 or x==0:return x
    start=0
    end=x
    while start<=end:
      mid=(start+end)//2
      if mid*mid==x:
        return mid
      elif mid*mid>x:
        end=mid-1
      else:
        start=mid+1
    return end