''' Time Complexity O(N)
Given a string s and an integer k, return true if you can use all the characters in s 
to construct k palindrome strings or false otherwise.
Example 1:

Input: s = "annabelle", k = 2
Output: true
Explanation: You can construct two palindromes using all characters in s.
Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"
'''
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        freq=[0]*26
        oddFreq=0
        for i in s:
            freq[ord(i)-ord('a')]+=1
        for i in range(26):
            if freq[i]%2==1:
                oddFreq+=1
        if oddFreq <= k and k <=len(s):
            return True
        return False