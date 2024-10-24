#Convert Date to Binary

class Solution:
    def convertDateToBinary(self, date: str) -> str:
        return '-'.join(bin(int(part))[2:] for part in date.split('-'))