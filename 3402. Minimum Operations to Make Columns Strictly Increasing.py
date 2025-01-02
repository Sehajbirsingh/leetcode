from typing import List

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        operations = 0
        
        for j in range(n):
            for i in range(1, m):
                if grid[i][j] <= grid[i-1][j]:
                    operations += (grid[i-1][j] - grid[i][j] + 1)
                    grid[i][j] = grid[i-1][j] + 1
        
        return operations

# Example usage:
solution = Solution()
print(solution.minimumOperations([[3,2],[1,3],[3,4],[0,1]]))  
print(solution.minimumOperations([[3,2,1],[2,1,0],[1,2,3]])) 