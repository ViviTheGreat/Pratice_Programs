#https://leetcode.com/problems/valid-parentheses/description/
#Brute Force
# Create a dict keeping track of all the brackets , and later check for closing and starting brackets
# Problem with this approch is it will not gurantee the correct order
####Failed Solution  
# class Solution:
#     def isValid(self, s: str) -> bool:
#         parenthesis = {"{":0,"}":0,"[":0,"]":0,"(":0,")":0}
#         for i in s:
#             if i in parenthesis:
#                 parenthesis[i] += 1
#         return (parenthesis["("]==parenthesis[")"] and parenthesis["{"]==parenthesis["}"] and parenthesis["["]==parenthesis["]"])

#Optimised Solution using Stack
## Store all the open brackets on a stack
## when a closing brackets comes validate the respective open bracket is on top of the stack.
## Validate till the end of the string and return true if stack is empty
## Few boundry conditions , like if string has only closing bracket than it needs to be handled properly

# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack =[]
#         openParenthesis = {"{":0,"[":0,"(":0}
#         closeParenthesis = {"}":"{","]":"[",")":"("}
#         for i in s:
#             if i in openParenthesis:
#                 stack.append(i)
#                 # parenthesis[i] += 1
#             elif i in closeParenthesis:
#                 if(len(stack)==0):
#                     return False
#                 else:
#                     if (stack[-1] != closeParenthesis[i]):
#                         return False
#                     else:
#                         stack.pop()
#         if(len(stack)!=0):
#             return False
#         else: 
#             return True

#More clean code would be to use parenthesis.values and parenthesis.keys
#With only one dict
#Theoritically it is slow but because total key:value pair is just 3 , it won't impact


class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        Parenthesis = {"}":"{","]":"[",")":"("}
        for i in s:
            if i in Parenthesis.values():   #If Open Parenthesis
                stack.append(i)
            elif i in Parenthesis:  #If Close Parenthesis
                if not stack or Parenthesis[i] != stack.pop():
                    return False
        return not stack


sol = Solution()        
print(sol.isValid("]"))

