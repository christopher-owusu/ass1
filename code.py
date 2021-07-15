from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (1 + right) // 2

            if target == nums[middle]:        
                return middle 

            if target > nums[middle]:   
                left = middle + 1  # check if target is greater than the middle value than start searching to the right
            else:
                right = middle - 1      # searching to the left

        return left       
