class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        num = n
        while(True):
            if(num % 2 == 0):
                return num
            num += n