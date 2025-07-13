'''6. Zigzag Conversion
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"'''
class Solution:
  def convert(self, s: str, numRows: int) -> str:
    if numRows==1:return s
    res=""
    for i in range(numRows):
      for j in range(i,len(s),(numRows-1)*2):
        res+=s[j]
        if(i>0 and i< numRows-1 and j+(numRows-i-1)*2 <len(s)):
          res+=s[j+(numRows-i-1)*2]
    return res