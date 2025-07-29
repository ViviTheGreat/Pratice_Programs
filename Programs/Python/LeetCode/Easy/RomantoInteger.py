#Roman to Integer
#https://leetcode.com/problems/roman-to-integer/description/

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
## Brute Force
class Solution:
    def romanToInt(self, s: str) -> int:
        dictRoman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}    #MCMXCIV
        result=0
        if(len(s) == 1):
            return int(dictRoman[s[0]])     # If a single character is present than just return single character value
        i =0    #Starts with i=0 to iterate amoung the string
        while(i<len(s)-1):  # Iterate till end of the string
            if(dictRoman[s[i]] >= dictRoman[s[i+1]]):   # if first character is greater than or equal than add those value , example VI  , add 5 to result
                result = result + dictRoman[s[i]]
                i += 1    
            elif(dictRoman[s[i]] < dictRoman[s[i+1]]):   # if first character is lesser than next character , substract value  , example IV  , substract 1 to result
                result = result  - dictRoman[s[i]]
                i += 1
        if(i == len(s)-1):        # If last characer is present than just add last character value
            result = result + dictRoman[s[i]]
        return result 

    
if __name__=="__main__":
    Sol = Solution()
    print(Sol.romanToInt("MCMXCIV"))