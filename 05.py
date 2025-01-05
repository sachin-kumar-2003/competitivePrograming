'''
You are given a string s of lowercase English letters and a 2D integer array shifts where shifts[i] = [starti, endi, directioni]. For every i, shift the characters in s from the index starti to the index endi (inclusive) forward if directioni = 1, or shift the characters backward if directioni = 0.
Shifting a character forward means replacing it with the next letter in the alphabet (wrapping around so that 'z' becomes 'a'). Similarly, shifting a character backward means replacing it with the previous letter in the alphabet (wrapping around so that 'a' becomes 'z').
Return the final string after all such shifts to s are applied.
Example 1:

Input: s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]
Output: "ace"
Explanation: Firstly, shift the characters from index 0 to index 1 backward. Now s = "zac".
Secondly, shift the characters from index 1 to index 2 forward. Now s = "zbd".
Finally, shift the characters from index 0 to index 2 forward. Now s = "ace".'''
from typing import List
class Solution:
  def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
    preFix=[0]*(len(s)+1)
    res=""
    for start,end,dire in shifts:
      if dire:
        preFix[start]-=1
        preFix[end+1]+=1
      else:
        preFix[start]+=1
        preFix[end+1]-=1
    diff=0               
    for i in range(len(preFix)-1,0,-1):
      diff+=preFix[i]
      res+=chr((ord(s[i-1])-ord('a')+diff)%26+ord('a'))
    return res[::-1]