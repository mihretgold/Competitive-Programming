class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = low + (high - low)//2
            if mid < len(arr) - 1 and arr[mid] > arr[mid+1]:
                high = mid - 1
            else:
                low = mid + 1

        return low