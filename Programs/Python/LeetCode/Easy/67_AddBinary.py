#https://leetcode.com/problems/add-binary
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # return str(bin(int(a)) | bin(int(b)))
        carry=0
        ans=[]
        if len(a)>=len(b):
            b = ("0" * (len(a)-len(b)+1)) + b
            a = "0" + a
        elif len(b)>len(a):
            a = ("0" * (len(b)-len(a)+1)) + a
            b = "0" + b
        # print(f"Before Adding {a} {b}")
        for i in range(len(a)-1,-1,-1):
            # print(f"Adding {a[i]} {b[i]}")
            if(int(a[i])+int(b[i])+carry==1):
                ans.append("1")
                carry=0
            elif(int(a[i])+int(b[i])+carry==2):
                # print(f"more {int(a[i])+int(b[i])+carry}")
                ans.append("0")
                carry =1
            elif(int(a[i])+int(b[i])+carry==3):
                # print(f"less than {int(a[i])+int(b[i])+carry}")
                ans.append("1")
                carry =1
            else:
                ans.append("0")
                carry=0
        ans = int(''.join(ans[-1::-1]))
        return str(ans)

    
sol = Solution()
print(sol.addBinary("1010","1011"))