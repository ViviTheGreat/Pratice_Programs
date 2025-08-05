#https://leetcode.com/problems/reverse-prefix-of-word

#Intution : Many ways to do this , will try all the ways.
#1st : Use find() function get index and using slice return it.
#1st : Iterate to the string and on fist occurance save the index , reverse the string using slice and return with appending the remaining string.
#2nd : Rather than iterating , just use the split function get the lenght of the first split word that would be the index , repeat as was done on the above approach.
#3rd : Use Stack , stack all the letters until the character is found , use done use the pop and slice aproach

# Best Solution - 100%
# class Solution:
#     def reversePrefix(self, word: str, ch: str) -> str:
#         if(word.find(ch) != -1):
#             return word[word.find(ch)::-1]+word[word.find(ch)+1:]
#         return word

#Still 100% solution
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for index , value in enumerate(word):
            if(value==ch):
                return word[index::-1]+word[index+1:]
        return word
    
sol = Solution()
print(sol.reversePrefix("vivek","1"))
    




        