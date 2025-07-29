#https://leetcode.com/problems/shuffle-string/

# You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
from typing import List 

#Brute Force
# class Solution:
#     def restoreString(self, s: str, indices: List[int]) -> str:
#         result = {}
#         for key,value in enumerate(s):
#             result[indices[key]]=value
#         resultString = []
#         for i in range(len(indices)):
#             resultString.append(result[i])
#         return ''.join(resultString)


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [0] * len(indices)     # Create a list with fix size
        for key,value in enumerate(s):
            result[indices[key]]=value  #Add the values in the list as per indices
        return ''.join(result)  # Convert list to string and return for result

sol = Solution()
print(sol.restoreString("codeleet",[4,5,6,7,0,2,1,3]))