# https://leetcode.com/problems/convert-date-to-binary
#Intution : Change number to binary using bin function , make sure it is properly converted
# from string to int to binary ,and it returns 
#As the format is fixed we can directly split and conver to binary
#yyyy-mm-dd
#Apprently this is very slow
class Solution:
    def convertDateToBinary(self, date: str) -> str:
        return (bin(int(date[0:4]))[2:])+"-"+(bin(int(date[5:7]))[2:])+"-"+(bin(int(date[8:]))[2:])
# Other way to write the code is through split function and changing them 
# to bin explicitly , not sure why 2nd solution is fast though 
# Feeling lazy to write the 2nd solution too , if required go and checkout on leetcode


sol=  Solution()
print(sol.convertDateToBinary("1900-01-01"))