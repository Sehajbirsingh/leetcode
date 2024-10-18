#leetcode 55 Jump game
"""You are given an integer array nums. You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
"""
#throug DP and Greedy
#DP saves memory as cache and tell that index[i]= False, until index[0] = False not possible
#O(n^2)
#greedy -> o(n)


def canJump(self, nums: List[int]) -> bool:
    # Initialize max_reach as 0 - initially we can only reach index 0
    max_reach = 0
    
    # Loop through array except last element (no need to jump from last element)
    # Example 1: nums = [2,3,1,1,4]
    # Example 2: nums = [3,2,1,0,4]
    for i in range(len(nums) - 1):
        
        # STEP 1: Check if current position is reachable
        # If we can't reach current index, it's impossible to move forward
        # Example 1: Always reachable as max_reach keeps increasing
        # Example 2: At i=4, we're stuck at max_reach=3, can't reach i=4
        if i > max_reach:
            return False
        
        # STEP 2: Update max_reach
        # max_reach = max(current_max_reach, current_position + jump_length)
        # Example 1:
        # i=0: max(0, 0+2) = 2   [can reach index 1,2]
        # i=1: max(2, 1+3) = 4   [can reach index 1,2,3,4]
        # i=2: max(4, 2+1) = 4   [already can reach end]
        
        # Example 2:
        # i=0: max(0, 0+3) = 3   [can reach index 1,2,3]
        # i=1: max(3, 1+2) = 3   [still can only reach till 3]
        # i=2: max(3, 2+1) = 3   [still stuck at 3]
        # i=3: max(3, 3+0) = 3   [can't move forward from 3]
        max_reach = max(max_reach, i + nums[i])
        
        # STEP 3: Early success check
        # If we can reach the last index from current position, return immediately
        # Example 1: At i=1, max_reach becomes 4, we can reach the end!
        # Example 2: max_reach never reaches 4, so this condition never triggers
        if max_reach >= len(nums) - 1:
            return True
    
    # STEP 4: Final check
    # If we complete the loop without returning:
    # - True: if max_reach can reach or exceed last index
    # - False: if max_reach falls short of last index
    # Example 1: Unnecessary (would return True)
    # Example 2: Returns False as max_reach(3) < last_index(4)
    return max_reach >= len(nums) - 1

# Full Example 1: [2,3,1,1,4]
# i=0: max_reach = 2  (can jump to index 1,2)
# i=1: max_reach = 4  (can reach end! return True)
# Result: True

# Full Example 2: [3,2,1,0,4]
# i=0: max_reach = 3  (can jump to index 1,2,3)
# i=1: max_reach = 3  (stuck at index 3)
# i=2: max_reach = 3  (still stuck)
# i=3: max_reach = 3  (completely stuck, can't reach 4)
# Result: False
