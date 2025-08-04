from typing import List

#Intution : Just iterate and check if ++ then add otherwise subsctract from x
#Best solution too B-)
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x=0
        for i in operations:
            if("++" in i):
                x += 1
            else:
                x -=1
        return x

sol = Solution()
print(sol.finalValueAfterOperations(["--X","X++","X++"]))