class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0 
        high = len(nums) -1
        left = len(nums) + 1
        while low <= high:
            # check
            mid = low + (high - low)//2
            if nums[mid] == target:
                left = min(left, mid)
                high = mid - 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        low = 0 
        high = len(nums) -1
        right = -1
        while low <= high:
            # check
            mid = low + (high - low)//2
            if nums[mid] == target:
                right = max(right, mid)
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        if left == len(nums) + 1:
            left = -1
        return [left, right]