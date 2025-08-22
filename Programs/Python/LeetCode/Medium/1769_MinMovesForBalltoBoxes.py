#https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box
# #Brute Force
# 100X
# both left / right distance of 1 from i and add 1 
# convert left side to integer and than proceed
# right side should be normal
#Initial thought ^ waste lot of time on this xD
from typing import List

### Below gives timeout 

# class Solution:
#     def minOperations(self, boxes: str) -> List[int]:
#         ans=[]
#         for i in range(len(boxes)):
#             lcount , rcount = 0,0
#             #Calculating left side
#             lstring = boxes[:i]
#             if len(lstring)>0:
#                 for ls in range(len(lstring)):
#                 # while(ls < len(lstring)):
#                     if(lstring[::-1][ls]=="1"):
#                         lcount +=ls+1
#             #Calculating right side
#             rstring = boxes[i+1:]
#             if(len(rstring)>0):
#                 for rs in range(len(rstring)):
#                 # while(rs<len(rstring)):
#                     if(rstring[rs]=="1"):
#                         rcount +=rs+1
#             ans.append(lcount+rcount)
#         return ans





#Brute force , very less complicated taking benifit of abs() function
    
#3088 Beats 17.94%

#17.99MB Beats 74.89%
#17.85 MB Beats 92.73% , replacing len(boxes) to n 

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0]*n
        for i in range(n):
            for j in range(n):
                    if boxes[j]=="1":   
                        ans[i]+=abs(i-j)
        return ans
    
sol = Solution()
print(sol.minOperations("001011"))

