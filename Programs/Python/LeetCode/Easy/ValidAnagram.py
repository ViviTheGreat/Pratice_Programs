from collections import Counter


class Solution:
    # Brute force
    # Just compare the sorted character 
    # def isAnagram(self, s: str, t: str) -> bool:
    #     return (sorted(s) == sorted(t))

    
    #Optimised solution
    # Counter function counts the character and the occurance of that character
    # and we finally just comare those 2 dict
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):   # If length is not equal just return -1
            return False
        a=Counter(s)
        b=Counter(t)
        return a == b

    
Sol = Solution()
print(Sol.isAnagram("ggii","iigg"))
