#https://leetcode.com/problems/reverse-degree-of-a-string

#ord(a) is 97 and ord(z) is 122 keeping that in mind , have that in formula , beats 97%
class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += (123-ord(s[i]))*(i+1)
        return res
    
#Better solution might be to use enumerate , not too good just 37%
# class Solution:
#     def reverseDegree(self, s: str) -> int:
#         res = 0
#         for i , v in enumerate(s):
#             res += (ord("z")+1-ord(v))*(i+1)
#         return res

sol = Solution()
print(sol.reverseDegree("zaza"))