'''3169. Count Days Without Meetings
You are given a positive integer days representing the total number of days an employee is available for work (starting from day 1). You are also given a 2D array meetings of size n where, meetings[i] = [start_i, end_i] represents the starting and ending days of meeting i (inclusive).
Return the count of days when the employee is available for work but no meetings are scheduled.
Note: The meetings may overlap.
Example 1:
Input: days = 10, meetings = [[5,7],[1,3],[9,10]]
Output: 2
Explanation:
There is no meeting scheduled on the 4th and 8th days.'''
from collections import List
class Solution:
  def countDays(self, days: int, meetings: List[List[int]]) -> int:
    freeDays=0
    prevEnd=0
    for start,end in sorted(meetings):
      if start>prevEnd:
        freeDays+=start-prevEnd-1
      prevEnd=max(prevEnd,end)
    return freeDays+max(0,days-prevEnd)