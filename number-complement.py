class Solution:
    def findComplement(self, num: int) -> int:
        x = 1
        n = num 

        for i in range(n.bit_length()):
                num ^= (1 << i)
            
        return num