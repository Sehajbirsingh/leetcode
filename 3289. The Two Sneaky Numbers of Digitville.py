#3289. The Two Sneaky Numbers of Digitville

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        return [n for n in set(nums) if nums.count(n) > 1]