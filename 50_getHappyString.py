'''1415. The k-th Lexicographical String of All Happy Strings of Length n
A happy string is a string that:
consists only of letters of the set ['a', 'b', 'c'].
s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings
"aa", "baa" and "ababbc" are not happy strings.
Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.
Return the kth string of this list or return an empty string if there are less than k happy strings of length n.
Example 1:
Input: n = 1, k = 3
Output: "c"
Explanation: The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".'''
class Solution:
  def getHappyString(self, n: int, k: int) -> str:
    res=[]
    def backtrack(strg):
      if len(strg)==n:
        res.append(strg)
        return
      if len(strg)>n:return
      for char in 'abc':
        if strg=='':backtrack(char)
        elif strg and strg[-1]!=char:backtrack(strg+char)  
    backtrack('')
    res.sort()
    return res[k-1] if len(res)>=k else ''