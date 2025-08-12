#https://leetcode.com/problems/make-the-string-great

class Solution:
    def makeGood(self, s: str) -> str:
        stack , index = [s[0]] , 1
        while(index < len(s)):
            stack.append(s[index])
            # print(stack)
            if len(stack)>1 :
                if ((stack[-2].islower() and stack[-1].isupper()) or (stack[-1].islower() and stack[-2].isupper())) and (stack[-2].lower()==stack[-1].lower()):
                    stack.pop()
                    stack.pop()
            index += 1
            
        return ''.join(stack)
    
sol = Solution()
# print(sol.makeGood("abBAcC"))
print(sol.makeGood("pP"))
        