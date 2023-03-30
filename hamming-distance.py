class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = x ^ y
        return ans.bit_count()