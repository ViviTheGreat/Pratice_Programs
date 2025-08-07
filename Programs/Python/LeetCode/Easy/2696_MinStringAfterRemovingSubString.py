#https://leetcode.com/problems/minimum-string-length-after-removing-substrings


class Solution:
    def minLength(self, s: str) -> int:
        result , i  = [s[0]] , 1
        while i<len(s) :
            result.append(s[i])
            if len(result)>1:
                if (result[-1] == 'B' and result[-2] == 'A') or (result[-1] == 'D' and result[-2] == 'C'):
                    result.pop()
                    result.pop()
            i += 1
        return len(result)