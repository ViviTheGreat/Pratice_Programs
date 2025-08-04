# https://leetcode.com/problems/score-of-a-string
# Make a note mathmatically absolute difference is positive difference between two numbers
# irrespective of which number is bigger / smaller

class Solution:
    def scoreOfString(self, s: str) -> int:
        sum=0
        #Though S could be 1 also , 
        #Need to read program more carefully
        # if len(s)==1:
        #     return ord(s)
        for i in range(len(s)-1):
            sum += abs(ord(s[i])-ord(s[i+1]))
        return sum

sol = Solution()
print(sol.scoreOfString("12"))