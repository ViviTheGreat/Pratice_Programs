#https://leetcode.com/problems/split-a-string-in-balanced-strings
#Brute force
#Try to run a loop keep track of r and l count if balance breaks reset the value
#keep a track of count which will keep balance string count
#Question was not properly read , it just need to count number of L and R occurance in any manner, if it matches than increase the
#count
#beats 100%
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r , l , res = 0 , 0 , 0
        for i in range(len(s)):
            if s[i] == "R":
                r +=1
            elif s[i] == "L":
                l +=1
            if r==l :
                res +=1
        return res
    
sol = Solution()
print(sol.balancedStringSplit("RRLR"))
# RL RRLL RL RL



        