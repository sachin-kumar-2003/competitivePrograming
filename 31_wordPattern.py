'''Time Complexity O(N)
Word Pattern
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a
letter in pattern and a non-empty word in s. Specifically:
Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.
Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Explanation:
The bijection can be established as:
'a' maps to "dog".
'b' maps to "cat".'''
class Solution:
  def wordPattern(self, pattern: str, s: str) -> bool:
    visitedWord=set()
    pArr=list(pattern)
    sArr=s.split(' ')
    if len(pArr)!=len(sArr):return False
    hashMap={}
    for i in range(len(pArr)):
      if pArr[i] not in visitedWord:
        if sArr[i] in hashMap.values():return False
        hashMap[pArr[i]]=sArr[i]
        visitedWord.add(pArr[i])
      elif sArr[i] != hashMap[pArr[i]]:
        return False
    return True