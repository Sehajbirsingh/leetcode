class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # Iterate over possible number of operations (k)
        for k in range((len(nums) + 2) // 3 + 1):
            # Remove 3*k elements from the front
            sub = nums[3*k:]
            # Check if the remaining subarray is distinct
            if len(sub) == len(set(sub)):
                return k
        # If no distinct subarray is found, return the maximum possible operations
        return (len(nums) + 2) // 3