class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        store = set(nums)
        n = len(nums)
        
        for i in range(2 ** n + 1):
            binary = bin(i)[2:]
            length = len(binary)
            size = n - length
            string = ""
            for _ in range(size):
                string += "0"
                
            string += binary
            if string not in store:
                return string
            
        return ""
        
        