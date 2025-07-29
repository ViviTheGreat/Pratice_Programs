#Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


## Program Starts
## Brute Force

from typing import List


# Brute Force aparantly is also one of the best solutions
### Idea is to fetch every character from first string and compare with every character at same index with other string
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         commonString =[] # This will be started as empty and populated as we iterate
#         for compareStringIndex , compareString in enumerate(strs[0]): # This fetches the character and the index from the first string
#             print(f"Index : {compareStringIndex} , Values : {compareString}")
#             for i in range(1,len(strs)): # Compares with all the string , starts from 2nd string
#                 # print(f"Value of i : {i} and character of string is {strs[i][compareStringIndex]} and compare string is {compareString}")
#                 try:
#                     if strs[i][compareStringIndex] != compareString:
#                         return ''.join(commonString)    #Where the match fails we return common string so far
#                 except:
#                         return ''.join(commonString)    #Handle in case we get IndexOutOfBound that if 1st string length is shorter than any other
#             commonString.append(compareString)          # Append the common characters
#             print(f"Appended the string {commonString}")
#         return ''.join(commonString)                    # This could happen if 1st string all character matches with rest.



# Optimised Solution
# We sort the list and just compare the 2 strings the first and the last.
# Ideally this should take lesser time than to compare with all the strings
# This too is fast just like the older solutions

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commonString =[] # This will be started as empty and populated as we iterate
        strs.sort()
        # print(f"Sorted String : {strs}")
        for compareStringIndex , compareString in enumerate(strs[0]): # This fetches the character and the index from the first sorted string
            # print(f"Index : {compareStringIndex} , Values : {compareString}")
            # print(f"First : {strs[0][compareStringIndex]} , Last : {strs[len(strs)-1][compareStringIndex]}")
            try:
                if strs[0][compareStringIndex] != strs[len(strs)-1][compareStringIndex]:
                    return ''.join(commonString)
            except:
                    return ''.join(commonString)
            commonString.append(strs[0][compareStringIndex])
        return ''.join(commonString)

if __name__=="__main__":
    solu = Solution()
    print(solu.longestCommonPrefix(["abcd","ab","abcde","abcd","abcd","abcde"]))