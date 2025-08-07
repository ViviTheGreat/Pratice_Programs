# https://leetcode.com/problems/count-the-number-of-consistent-strings/?envType=problem-list-v2&envId=nsc52aki
from typing import List

#Intuition just run two loops and check , if char of word not in allowed than
#decrease the count , beats 95% 
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = len(words)
        for word in words:
            for char in word:
                if char not in allowed:
                    count -=1
                    break
        return count

    
sol = Solution()
print(sol.countConsistentStrings("ab",["a","ab","asdasd","bb","aa","aaaabbbb"]))
        