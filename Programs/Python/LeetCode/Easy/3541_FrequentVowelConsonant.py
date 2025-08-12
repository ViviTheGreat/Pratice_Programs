#https://leetcode.com/problems/find-most-frequent-vowel-and-consonant
#Intuition : set 2 dict consonants and vowels , iterate through the string create these two dict
#once done just return the max count of the values of dict
# class Solution:
#     def maxFreqSum(self, s: str) -> int:
#         c = {0:0}
#         v = {0:0}
#         for i in s:
#             if (i.lower() in "aeiou"):
#                 v.setdefault(i,0)
#                 v[i] += 1
#             else:
#                 c.setdefault(i,0)
#                 c[i] += 1
#         return max(c.values()) + max(v.values())

#Fine tuning : rather than using setdefault use if condition of v.get[i] which return True/False
#Beats 64.69% , fastest one is the same code but not sure why it is still not 100 :/
class Solution:
    def maxFreqSum(self, s: str) -> int:
        c = {0:0}
        v = {0:0}
        vow = ("a","e","i","o","u")
        for i in s:
            if (i.lower() in vow):
                if v.get(i):
                    v[i] += 1
                else:
                    v[i] = 1
            else:
                if c.get(i):
                    c[i] += 1
                else:
                    c[i]=1
        return max(c.values()) + max(v.values())
    

sol = Solution()
print(sol.maxFreqSum("aeiaeia"))
        