class Solution:
    def reverse(self, s, left, right):
        if left < right:
            s[left], s[right] = s[right], s[left]
            self.reverse(s, left+1, right-1)

        return
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1
        self.reverse(s, left, right)