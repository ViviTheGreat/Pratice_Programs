#https://leetcode.com/problems/number-of-good-pairs

from typing import List

#Intuition: Run 2 loops maintaining the index , beats only 17% , as soon as i have shorted variable it beats 100%,
## Lesson learnt , always have short variable name in loops
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result =0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if(nums[i]==nums[j]):
                    result += 1
        return result
sol = Solution()
print(sol.numIdenticalPairs([1,1,1,1]))