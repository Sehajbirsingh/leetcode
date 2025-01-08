class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
         unique_elements = set(nums)
         operations = 0

         for num in unique_elements:
             if num > k:
                 operations += 1
             elif num < k:
                 return -1

         return operations