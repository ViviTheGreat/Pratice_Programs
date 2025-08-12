# https://leetcode.com/problems/permutation-difference-between-two-strings/description
#Intuition : first iterataion create a dictionary of s with key as character and value as index
#second iteration just itereate through t and subsctract it with the index of dict
#Beats 100% , took 9 mins without any pressure , along with writting extra steps
from typing import List

class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        dict={}
        res = 0
        for i in range(len(s)):
            dict[s[i]]=i
        for j in range(len(t)):
            res += abs(j-dict[t[j]])
        return res
    
sol = Solution()
print(sol.findPermutationDifference("abcde","edbac"))