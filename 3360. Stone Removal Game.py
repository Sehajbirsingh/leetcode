class Solution:
    def canAliceWin(self, n: int) -> bool:
        count = 0
        pile = 10

        while n >= pile:
            n -= pile
            pile -= 1
            count += 1

        return count % 2 != 0

# Example usage
if __name__ == "__main__":
    n = int(input("Enter the number of stones: "))
    solution = Solution()
    print(solution.canAliceWin(n))