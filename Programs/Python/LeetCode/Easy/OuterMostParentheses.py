#https://leetcode.com/problems/remove-outermost-parentheses
#Brute Force : Navigate from left and keep track of parethese once done keep the string and repeat the same from left side
## Dropping the above way as it is over complicated , 
## Calculating the count where ( adds +1 and ) subs -1 from count keep track of string and return the resultant string
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        start , end , count = 0,len,0
        a=[]
        for i in range(len(s)):
            if(s[i]=='(') and count==0:
                start=i
                count += 1
            elif(s[i]=='(') and count!=0:
                count += 1
            elif(s[i]==')' and count==1):
                end=i
                count -=1
                a.append(s[start+1:end])
            elif(s[i]==')' and count!=1):
                count -=1
            # print(count)
        return(''.join(a))
## Apprently 
sol = Solution()
print(sol.removeOuterParentheses("(()())(())(()(()))"))