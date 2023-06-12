class Solution:
    def minimizeArrayValue(self, A: List[int]) -> int:
        prefix = accumulate(A)
        maxi = 0

        for index, value in enumerate(prefix):
            ans = (value + index) // (index + 1)
            maxi = max(ans, maxi)
        
        return maxi