'''Given two positive integers left and right, find the two integers num1 and num2 such that:
left <= num1 < num2 <= right .
Both num1 and num2 are prime numbers.
num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
Return the positive integer array ans = [num1, num2].
If there are multiple pairs satisfying these conditions,
return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].
Example 1:
Input: left = 10, right = 19
Output: [11,13]
Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
Since 11 is smaller than 17, we return the first pair.'''
from typing import List
class Solution:
  def closestPrimes(self, left: int, right: int) -> List[int]:
    notPrimes=[True]*(right+1)
    primes=[]
    for i in range(2,right+1):
      if notPrimes[i]:
        primes.append(i)
        start=2
        while i*start<=right:
          notPrimes[i*start]=False
          start+=1
    first,second,diff=-1,-1,float('inf')
    for i in range(len(primes)-1):
      if primes[i]>=left and primes[i+1]-primes[i]<diff :
        diff=primes[i+1]-primes[i]
        first,second=primes[i],primes[i+1]
    return [first,second]
