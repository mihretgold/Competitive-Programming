class Solution:
    def findBit(self, n):
        if n == 1:
            return "0"
        s = self.findBit(n-1)
        a = s + "1"
        string = ""
        for index in range(len(s)):
            if s[index] == "0":
                string += "1"
            else:
               string += "0"
               
        return a + string[::-1]

    def findKthBit(self, n: int, k: int) -> str:
        s = self.findBit(n)
        return s[k-1]