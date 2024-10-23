# 3285. Find Indices of Stable Mountains
class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        return[h for h in range(1,len(height)) if height[h-1] > threshold]