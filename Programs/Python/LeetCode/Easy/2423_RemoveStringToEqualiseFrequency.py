#https://leetcode.com/problems/remove-letter-to-equalize-frequency/

#Intuition : just create a dict and make sure frequency of that character is 1 , if it becomes
# 2 than we can mark return is True but if another character appears with value as 2 break the loop
# and return False 
#Not read the question properly , frequency could be more repeated characters too
class Solution:
    def equalFrequency(self, word: str) -> bool:
        dict = {}
        freq=0
        s=set()
        ## Storing all the characters in dict
        for i in word:
            if (not dict.get(i)):
                dict[i]=1
                if freq==0:
                     freq=1
            else:
                dict[i]  = dict.get(i) + 1
                if freq<dict[i]:
                    freq += 1
            ## Maximum occurance will be marked as freq
            ## check if anything any value is either freq+1 or 1 then return true else false
        # for j in dict.values():
        #     s.add(j)
        # if len(s)>2:
        #     False
        # elif len(s)==2: #aab or abcc
        #     for k in s:
        #         if k < freq:
        #             if k!=1 or k!=freq-1:
        #                  False
        
        # elif len(s)==1 and len(dict)!=1 and freq!=1: #aabb --> aab False or aabbcc -->aabbc False
        #             print(freq)
        #             return False
        # return True
        print(dict.values())
        for j in dict.values():
            if j!=freq:
                return (j==freq-1)
            elif j

sol = Solution()
print(sol.equalFrequency("ddaccb"))

#2,2,2,2,2,2
#2,1,2,1