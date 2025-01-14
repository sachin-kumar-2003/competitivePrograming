'''
You are given a 0-indexed string array words.
if str1 is both prefix and a suffix of str2 return the count .
words = ["a","aba","ababa","aa"]
Output: 4
Explanation: In this example, the counted index pairs are:
i = 0 and j = 1 because isPrefixAndSuffix("a", "aba") is true.
i = 0 and j = 2 because isPrefixAndSuffix("a", "ababa") is true.
i = 0 and j = 3 because isPrefixAndSuffix("a", "aa") is true.
i = 1 and j = 2 because isPrefixAndSuffix("aba", "ababa") is true.
Therefore, the answer is 4.
'''
from typing import List
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    ans+=1
        return ans
