# #Brute Force
# 100X
# both left / right distance of 1 from i and add 1 
# convert left side to integer and than proceed
# right side should be normal

# Use stack to keep track of 1s

from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans=[]
        for i in range(len(boxes)):
            lcount , rcount = 0,0
            #Calculating left side
            lstring = boxes[:i]
            if len(lstring)>0:
                for ls in range(len(lstring)):
                # while(ls < len(lstring)):
                    if(lstring[::-1][ls]=="1"):
                        lcount +=ls+1
            #Calculating right side
            rstring = boxes[i+1:]
            if(len(rstring)>0):
                for rs in range(len(rstring)):
                # while(rs<len(rstring)):
                    if(rstring[rs]=="1"):
                        rcount +=rs+1
            ans.append(lcount+rcount)
        return ans

sol = Solution()
print(sol.minOperations("110"))




# class Solution:
#     def minOperations(self, boxes: str) -> List[int]:
#         n = len(boxes)
#         left = [0] * n
#         right = [0] * n
#         cnt = 0
#         for i in range(1, n):
#             if boxes[i - 1] == '1':
#                 cnt += 1
#             left[i] = left[i - 1] + cnt
#         cnt = 0
#         for i in range(n - 2, -1, -1):
#             if boxes[i + 1] == '1':
#                 cnt += 1
#             right[i] = right[i + 1] + cnt
#         return [a + b for a, b in zip(left, right)]  




        