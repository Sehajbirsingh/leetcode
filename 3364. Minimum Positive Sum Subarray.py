class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        min_positive_sum = float('inf')
        
        # Iterate through possible subarray sizes
        for size in range(l, r + 1):
            # Use sliding window to find the sum of subarrays of the current size
            current_sum = sum(nums[:size])
            if current_sum > 0:
                min_positive_sum = min(min_positive_sum, current_sum)
            
            for i in range(size, n):
                current_sum += nums[i] - nums[i - size]
                if current_sum > 0:
                    min_positive_sum = min(min_positive_sum, current_sum)
        
        # Return the result
        return min_positive_sum if min_positive_sum != float('inf') else -1
