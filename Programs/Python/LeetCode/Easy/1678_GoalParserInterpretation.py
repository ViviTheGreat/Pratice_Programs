#https://leetcode.com/problems/goal-parser-interpretation

class Solution:
    #Intuition : iterate and keep track of what you get and just change to string using if else statment
    #Iterate through string keep track of 'G' 'l' and ')' and append to a list
    #Beats 24.95%
    # def interpret(self, command: str) -> str:
    #     res = []
    #     al = False
    #     for i in command:
    #         if i=="G":
    #             res.append("G")
    #         elif i=="l":
    #             al = True
    #         elif i==")" and not al:
    #             res.append("o")
    #         elif i==")" and al:
    #             res.append("al")
    #             al = False
    #     return ''.join(res)
## Should be best approach , though it still shows beats 56% 
    def interpret(self, command: str) -> str:
        res = []
        i=0
        al = False
        while (i<len(command)):
            if command[i]=="G":
                res.append("G")
                i +=1
            elif command[i:i+2]=="()":
                res.append("o")
                i +=2
            elif command[i:i+4]=="(al)":
                res.append("al")
                i +=4
        return ''.join(res)
    
sol = Solution()
print(sol.interpret("(al)G()()()()"))




        