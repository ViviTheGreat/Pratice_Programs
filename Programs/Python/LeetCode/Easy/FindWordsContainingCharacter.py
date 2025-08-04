#https://leetcode.com/problems/find-words-containing-character

from typing import List

#Straight forward
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result =[]
        for index , value in enumerate(words):
            if x in value:
                result.append(index)
        return result
    
sol = Solution()
print(sol.findWordsContaining(["vivek","is","the","best"],"e"))