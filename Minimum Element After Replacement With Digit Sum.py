#Minimum Element After Replacement With Digit Sum

class Solution:
    def minElement(self, nums: List[int]) -> int:
        replacement=[]
        for n in nums:
            sum_digit=sum(int(digit) for digit in str(n))
            replacement.append(sum_digit)

        return min(replacement)
