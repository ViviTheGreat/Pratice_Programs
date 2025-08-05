# https://leetcode.com/problems/clear-digits/?envType=problem-list-v2&envId=n1o5b42g
#First Intuition was to itirate through the string and slice it till you get the answer
#Problem is the slice was not correctly handled and was causing out of index
# Swtiched to stack approach and it worked - 100%
class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if (s[i] >= "0" and s[i]<="9"):
                stack.pop()
            else:
                stack.append(s[i])

        return ''.join(stack)

#Apprently this is slow 
# class Solution:
#     def clearDigits(self, s: str) -> str:
#         s = list(s)
#         i =0
#         while(i<len(s)):
#             if(s[i].isdigit()):
#                 del s[i]
#                 del s[i-1]
#                 i -= 1
#             else:
#                 i += 1
#         return "".join(s)
    
sol = Solution()
# print(sol.clearDigits("aksdjh123jkashk21"))
print(sol.clearDigits("aa22"))