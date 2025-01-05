from math import gcd
from functools import reduce
from typing import List

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        def lcm(a, b):
            return a * b // gcd(a, b)
        
        max_len = 0
        n = len(nums)
        
        for i in range(n):
            sub_prod = 1
            sub_gcd = nums[i]
            sub_lcm = nums[i]
            
            for j in range(i, n):
                sub_prod *= nums[j]
                sub_gcd = gcd(sub_gcd, nums[j])
                sub_lcm = lcm(sub_lcm, nums[j])
                
                if sub_prod == sub_gcd * sub_lcm:
                    max_len = max(max_len, j - i + 1)
        
        return max_len