#Find X-Sum of All K-Long Subarrays I

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
                # Initialize the result array
        answer = []
        
        # Iterate over all possible subarrays of length k
        for i in range(len(nums) - k + 1):
            # Extract the subarray of size k
            subarray = nums[i:i + k]
            
            # Count the frequencies of elements in the subarray
            frequency = Counter(subarray)
            
            # Sort elements by frequency and then by value
            sorted_elements = sorted(frequency.items(), key=lambda item: (-item[1], -item[0]))
            
            # Take the top x elements
            top_x_elements = sorted_elements[:x]
            
            # Calculate the x-sum
            x_sum = sum(count * elem for elem, count in top_x_elements)
            
            # Append the x-sum to the result list
            answer.append(x_sum)
        
        return answer
