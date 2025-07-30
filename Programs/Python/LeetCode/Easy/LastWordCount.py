# 58. Length of Last Word
# https://leetcode.com/problems/length-of-last-word/description/

# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.

class Solution:
    # Brute Force
    # slice from left store the index without space will you again get a blank space 
    # that is the last string
    # return the length of the word
    def lengthOfLastWord(self, s: str) -> int:
        i = -1
        start , end=  -1 , -(len(s)+1)
        # print(f"{start} {end}")
        start_set = False
        while(i!=-(len(s)+1)):
            if(s[i]!=" " and not start_set):
                start , start_set =i , True
            elif(s[i]==" " and start_set):
                end=i
                break
            i -= 1
        return len(s[start:end:-1])
    
## Apparently the best code

sol = Solution()
print(sol.lengthOfLastWord("asdasd  asdasd  sdasdasd                        "))