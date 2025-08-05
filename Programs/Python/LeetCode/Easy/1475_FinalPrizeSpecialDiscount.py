from typing import List


#Intuition : Got the question itself wrong , it took lot of time , that's the reason 
# got it just working rather than thinking efficiently , beats just 5% :/
# 2 Loops which is used to compare and breaks when min value is found.
#Also 2 condition to take care of 
#1. if discount is not found then it should be as it is 
#2. if same value is found your value becaue 0 , that's the reason it could be 0 also
 
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = []
        for index , value in enumerate(prices):
            min=value
            isDiscount = False
            for compareIndex , compareValue in enumerate(prices[index+1:]):
                if( compareValue <= min):
                    min =  compareValue
                    isDiscount = True
                    break
            if(isDiscount):
                result.append(value-min)
            else:
                result.append(value)
        return result

#Thinking what else can be done
#Can you done using stack

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = []
        for index , value in enumerate(prices):
            min=value
            for compareIndex , compareValue in enumerate(prices[index+1:]):
                if( compareValue <= min):
                    min =  compareValue
                    result.append(value-min)
                    break
            else:
                result.append(value)
        return result


sol = Solution()
print(sol.finalPrices([8,4,6,2,3]))