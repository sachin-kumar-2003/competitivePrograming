'''Time Complexity O(N)
Max Sum of a Pair With Equal Sum of Digits
You are given a 0-indexed array nums consisting of positive integers. You can choose
two indices i and j, such that i != j, and the sum of digits of the number nums[i] is
equal to that of nums[j].
Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices
i and j that satisfy the conditions.
Example 1:
Input: nums = [18,43,36,13,7]
Output: 54
Explanation: The pairs (i, j) that satisfy the conditions are:
- (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
- (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
So the maximum sum that we can obtain is 54.'''
from typing import List
class Solution:
  def maximumSum(self, nums: List[int]) -> int:
    def digitSum(n):
      total=0
      while n:
        rem=n%10
        total+=rem
        n=n//10
      return total
    hashMap={}
    maxSum=-1
    for i in range(len(nums)):
      digitTotal=digitSum(nums[i])
      if digitTotal in hashMap:
        maxSum=max(maxSum,(hashMap[digitTotal])+nums[i])
        if hashMap[digitTotal]<nums[i]:hashMap[digitTotal]=nums[i]
      else:
        hashMap[digitTotal]=nums[i]
    return maxSum