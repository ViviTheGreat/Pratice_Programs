#https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
#Intution : 
#Inbuild python function : find() does the same thing
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

#Split the string with needle , the returning 1st list item length will be the index of needle
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if (len(haystack.split(needle)[0])!=len(haystack)):
            return len(haystack.split(needle)[0]) 
        else:
            return -1

sol = Solution()
print(sol.strStr("leetcode","leeto"))