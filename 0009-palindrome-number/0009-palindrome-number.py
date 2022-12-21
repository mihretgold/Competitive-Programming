class Solution:
    # Algorithm
    # s1: reverse number
    # s2: if number is same as the original return true else return false
    def isPalindrome(self, x: int) -> bool:
        if x<0 or x%10==0 and x!=0:
            return False
        rev=0
        while(x>rev):
            r=x%10
            rev=(rev*10) + r
            x=x//10
        if x==rev or x==rev//10:
            return True
        else: return False
    