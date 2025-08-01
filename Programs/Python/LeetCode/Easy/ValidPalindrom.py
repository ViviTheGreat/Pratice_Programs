#https://leetcode.com/problems/valid-palindrome

        #Brute Force Method
        #Traverse through the string , check the ascii value 
        # if between 65 - 90 i.e. upper case then convert to lower case and add to the list
        # if between 97 to 122 then just append to the list , also number from 0-9 is from 48 to 57
        # ignore anything other than this
        # finally when sting is in the list check if it is palindrom by reversing and checking if equal
class Solution:
    def isPalindrome(self, s: str) -> bool:
        str=[]
        for i in s:
            if(ord(i)>=65 and ord(i)<=90):
                str.append(i.lower())
            elif((ord(i)>=97 and ord(i)<=122) or (ord(i)>=48 and ord(i)<=57)):
                str.append(i)
        return str==str[-1::-1]
    
#Optimised solution is to use isalnum() rather than checking the ascii value , which is overhead
class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=""
        for i in s:
            if i.isalnum():
                a+=i.lower()
        return a[::]==a[::-1] 


sol = Solution()
print(sol.isPalindrome("Vi V"))