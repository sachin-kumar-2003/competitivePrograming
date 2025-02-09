'''Time Complexity O(N)
You are given a 0-indexed integer array nums. A pair of indices
(i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].
Return the total number of bad pairs in nums.
Input: nums = [4,1,3,3]
Output: 5
Explanation: The pair (0, 1) is a bad pair since 1 - 0 != 1 - 4.
The pair (0, 2) is a bad pair since 2 - 0 != 3 - 4, 2 != -1.
The pair (0, 3) is a bad pair since 3 - 0 != 3 - 4, 3 != -1.
The pair (1, 2) is a bad pair since 2 - 1 != 3 - 1, 1 != 2.
The pair (2, 3) is a bad pair since 3 - 2 != 3 - 3, 1 != 0.
There are a total of 5 bad pairs, so we return 5.'''
from typing import List
from collections import defaultdict
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        size=len(nums)
        count=0
        visitedCount=defaultdict(int)
        for i in range(size):
            count+=visitedCount[i-nums[i]]
            visitedCount[i-nums[i]]+=1
        return (size*(size-1)//2)-count