# https://leetcode.com/problems/truncate-sentence/
#Brute Force : reduce k when " " and return when 0 
# class Solution:
#     def truncateSentence(self, s: str, k: int) -> str:
#         ans = []
#         for i in range(len(s)):
#             if (s[i]==" "):
#                 k -= 1
#                 if (k==0):
#                     return "".join(ans)
#             ans.append(s[i])
#         return "".join(ans)
#Beats 100%
# class Solution:
#     def truncateSentence(self, s: str, k: int) -> str:
#         ans = ""
#         s = s.split(" ")
#         for i in range(k):
#             ans =ans+s[i]+" "
#         return(ans[:-1])
    
#More optimised code , beats 100% and 56% memory 
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(s.split()[:k])

sol = Solution()
print(sol.truncateSentence("hello world is this correct",2))