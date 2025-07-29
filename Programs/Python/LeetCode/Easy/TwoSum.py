# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


###### Program Starts ######

from typing import List

## Bruce Force Method
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         sum =0
#         for index_i , i  in enumerate(nums):
#             print(f"Index i {index_i} and value is {i}")
#             for index_j , j in enumerate(nums[index_i+1:],start=(index_i + 1)):
#                 print(f"Index i {index_i} and value is {i}")
#                 print(f"Index j {index_j} and value is {j}")
#                 if(i + j == target):
#                     return index_i,index_j
                
## Optimised Code

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map ={}
        for index , value in enumerate(nums):
            if (target - value) not in hash_map:
                hash_map[value] = index
            else:
                return [index , hash_map[target - value]]

if __name__ == "__main__":
    print("Start")
    check = Solution()
    print("Done")
    print(check.twoSum([3,3],6))