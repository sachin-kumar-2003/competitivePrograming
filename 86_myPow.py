'''50. Pow(x, n)
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000'''
class Solution:
  def myPow(self, x: float, n: int) -> float:
    if x == 0:return 0 if n > 0 else float('inf')
    if n < 0:
      x = 1 / x
      n = -n
    ans = 1
    while n > 0:
      if n % 2 == 1:
        ans *= x
      x *= x
      n //= 2
    return ans