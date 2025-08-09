#https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/
#Intuition : Create a dict and store number of occurance , maintain a repeatCount and halt the iteration if it reaches repeatCount
#Beats 100% B-)
#Though if we had read the question properly we would have known that numbers are going to be 
#from 0 to n-1 , we could have used that to write the same thing without dict.
 
from typing import List


class Solution:
    # def getSneakyNumbers(self, nums: List[int]) -> List[int]:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        dict = {}
        count = 0
        for i in nums:
            if(dict.setdefault(i,0) == 1):
                count +=1
            dict[i] += 1
            if count==2:
                break
        keys = [k for k, v in dict.items() if v == 2]
        return keys


sol = Solution()
print(sol.getSneakyNumbers([0,3,2,1,3,2]))