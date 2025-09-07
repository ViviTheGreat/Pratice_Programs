#https://leetcode.com/problems/sort-the-people/?envType=problem-list-v2&envId=nya3ag86
from typing import List

#Intuition : Create a dict to store these 2 different list and sort by keys and print the values
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d = dict()
        l = len(names)
        ans = [""]*l
        #Create Dict for mapping
        for i in range(l):
            d[heights[i]]=names[i]
        #Sort heights
        sortedList = sorted(heights,reverse=True)
        #Create answer list to return
        for j in range(l):
            ans[j] = d[sortedList[j]]
        return ans


        

sol = Solution()
print(sol.sortPeople(["vivek","shrivastava"],[189,178]))
        