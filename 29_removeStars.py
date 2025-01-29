''' Time Complexity O(N)
Problem : Removing Stars From a String
You are given a string s, which contains stars *.
In one operation, you can:
Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Example 1:
Input: s = "leet**cod*e"
Output: "lecoe"
Explanation: Performing the removals from left to right:
- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
There are no more stars, so we return "lecoe".'''
class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for i in  range(len(s)):
            if s[i]=="*":
                stack.pop()
            else:
                stack.append(s[i])
        return ''.join(stack)