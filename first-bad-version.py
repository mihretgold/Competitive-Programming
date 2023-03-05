# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 0 
        high = n
        while low <= high:
            mid = low + (high - low)//2
            if isBadVersion(mid) and (mid == 0 or not isBadVersion(mid-1)):
                return mid
            elif not isBadVersion(mid):
                low = mid + 1
            else:
                high = mid - 1

        return 1