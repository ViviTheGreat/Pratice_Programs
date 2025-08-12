#https://leetcode.com/problems/fruits-into-baskets-ii
from collections import deque
from typing import List
#Intuition : 2 For loops , change the value of bucket capacity where it validates the condition and mannage count
#Matches with the top most logic
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        useBasket =0
        for fvalue in fruits:
            for bindex , bvalue in enumerate(baskets):
                if (fvalue <= bvalue):
                    baskets[bindex]=0
                    useBasket +=1
                    break
        return len(baskets)-useBasket

sol = Solution()
print(sol.numOfUnplacedFruits([3,6,1],[6,4,7]))                    
            

