class Solution:
    # Algorithm
    # s1: reverse number
    # s2: if number is same as the original return true else return false
     def isPalindrome(self, x: int) -> bool:
            if x<0:
                return False
            
            num_original=x
            rev=0
            while(x>0):
                r=x%10
                rev=(rev*10) + r
                x//=10
            return num_original==rev
        