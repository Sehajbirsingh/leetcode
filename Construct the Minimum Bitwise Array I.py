# Construct the Minimum Bitwise Array I
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        def check_number(n: int) -> int:
            # Try numbers from 0 to n to find smallest x where x OR (x+1) = n
            # We can optimize by only checking up to n since x OR (x+1) ≥ x+1
            for x in range(n):
                if x | (x + 1) == n:
                    return x
            return -1
        
        def is_power_of_two(n: int) -> bool:
            return n & (n - 1) == 0
        
        ans = []
        for num in nums:
            # Key observations:
            # 1. If num is power of 2, no solution exists
            # 2. For x OR (x+1) = num, x must be less than num
            if is_power_of_two(num):
                ans.append(-1)
                continue
                
            result = check_number(num)
            ans.append(result)
            
        return ans