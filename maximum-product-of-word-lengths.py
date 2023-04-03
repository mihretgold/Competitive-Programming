class Solution:
    def maxProduct(self, words: List[str]) -> int:
        maxi = 0
        length = len(words)
        nums = []
        
        for index in range(length):
            unique = 0
            for letter in words[index]:
                unique |= 1 << (ord(letter) - 97)
            nums.append(unique)

        for index in range(length):
            check = nums[index]
            for i in range(index+1, length):
                if check & nums[i] == 0: 
                    maxi = max(maxi, len(words[index])*len(words[i]))

        return maxi