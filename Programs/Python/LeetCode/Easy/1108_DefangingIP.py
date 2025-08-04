# https://leetcode.com/problems/defanging-an-ip-address
# Brute Force : directly using the inbuilt replace function
# class Solution:
#     def defangIPaddr(self, address: str) -> str:
#         address = address.replace(".","[.]")
#         print(address)

#Below is slightly better , though can also be used as concatenation
class Solution:
    def defangIPaddr(self, address: str) -> str:
        result=[]
        for i in range(len(address)):
            if address[i]!=".":
                result.append(address[i])
            else:
                result.append("[")
                result.append(".")
                result.append("]")
        return(''.join(result))



sol = Solution()
print(sol.defangIPaddr("1.1.1.1"))