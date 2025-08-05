#https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/?envType=problem-list-v2&envId=n1o5b42g
#Intuition : Keep a track of stack which stacks "(" and pop(s) ")" , also track maximum of stack size
# 100% B-)
class Solution:
    def maxDepth(self, s: str) -> int:
        stack , max = [] , 0 
        for i in s:
            if i == '(': 
                stack.append("(")
                if (len(stack)>max):
                    max = len(stack)
            elif i == ')':
                    stack.pop()
        return max
    
sol = Solution()
print(sol.maxDepth("(1+(2*3)+((8)/4))+1"))


