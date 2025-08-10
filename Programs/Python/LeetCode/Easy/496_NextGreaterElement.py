#https://leetcode.com/problems/next-greater-element-i/?envType=problem-list-v2&envId=n1o5b42g
#
from typing import List
## Intuition : Create a result array = len.nums * [-1]
## iterate each value of nums1 and find index in nums2 , starting that point iterate till len(nums2) if found update the value in result array otherwise just leave it
#This was most bad way to do , only beats 5% - O(n*m*k)
# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         result = [-1] * len(nums1)
#         for i in range(len(nums1)):
#             for j in range(len(nums2)):
#                 if nums1[i]==nums2[j]: 
#                     for k in range(j+1,len(nums2)):
#                         if nums2[k]>nums2[j]:
#                             print(f"Value {nums2[k]} is greater than {nums2[i]}")
#                             result[i]=nums2[k]
#                             break
#         return result
    
#Let's try with monotonic approach
#Try to undestand the concept here : https://www.youtube.com/watch?v=Dq_ObZwTY_Q&ab_channel=AlgoMonster
#Beats 100% , Revise
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res = {}
        for i in nums2[::-1]:
            while stack and i > stack[-1]:
                stack.pop()
            if not stack:
                res[i] = -1
            else:
                res[i]=stack[-1]
            stack.append(i)
        ans=[]
        for i in nums1:
            ans.append(res[i])
        return ans
    
sol = Solution()
print(sol.nextGreaterElement([1,3],[1,3,4,2]))        