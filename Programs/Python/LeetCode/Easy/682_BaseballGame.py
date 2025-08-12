#https://leetcode.com/problems/baseball-game
# Stack String 
from typing import List
#Intuition : Just iterate and store in a list , pop in case 'C' comes up and in the end just sum of all the item in the list
#lesson learnt : isinstance(int(value),int) : checks the string of int is int or not
# Or simply keep that on else statement

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = [])
        for value in operations:
            if value=='+':
                score.append(int(score[-1])+int(score[-2]))
            elif value=='C':
                score.pop()
            elif value=='D':
                score.append(int(score[-1])*2)
            elif isinstance(int(value),int):
                score.append(value)
        result =0
        for i in score:
            result +=int(i)
        return result
    
sol = Solution()
print(sol.calPoints(["5","2","C","D","+"]))