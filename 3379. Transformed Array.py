from typing import List

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        
        for i in range(n):
            if nums[i] > 0:
                new_index = (i + nums[i]) % n
            elif nums[i] < 0:
                new_index = (i + nums[i]) % n
            else:
                new_index = i
            
            result[i] = nums[new_index]
        
        return result