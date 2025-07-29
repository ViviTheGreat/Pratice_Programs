# 1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence
# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/description/

# Brute Force Method and apparently the best 
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split()     # Split the sentence into list with single space i.e words
        for i in range(len(sentence)):
            if(searchWord == sentence[i][:len(searchWord)]):    #Match the searchWord and match with index of the list storing words
                return(i+1)     #Answer should be with human index and not the programming index ;)
        return -1
        

sol = Solution()
print(sol.isPrefixOfWord("vivek is the best the","th"))
