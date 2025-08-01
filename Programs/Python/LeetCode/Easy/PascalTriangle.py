from typing import List

# Brute Force
# Run 2 loops , first for each element on the list and other the actual list
# Initialise the actual list with all 1 , first and last element is anyway going to be 1
#Inside loop will run from 2nd index till (Last-1) index which will update the value with 
# Sum of element i and i-1 of previous element
#
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[]
        insideList=[]
        for i in range(numRows):
            insideItem = [1] * (i+1)    # Fixing the first and the last element to 1
            for j in range(1,i):       # Updating the middle items
                insideItem[j] = ans[i-1][j]+ans[i-1][j-1]
            ans.append(insideItem)
            insideItem=[]   # Clearing Inside Item
        return(ans)
sol = Solution()
print(sol.generate(5))