
#https://leetcode.com/problems/maximum-69-number
#Intuition : Just change 6 to 9 starting from left to right , return same number if no change
#Make sure to typecast to int
#Beats 100%
class Solution:
    def maximum69Number (self, num: int) -> int:
        max = num 
        max = list(str(max))
        num = list(str(num))
        for i in range(len(num)):
            if num[i]=='6':
                max[i]='9'
                return int(''.join(max))
        return int(''.join(num))

sol = Solution()
print(sol.maximum69Number(9696))

