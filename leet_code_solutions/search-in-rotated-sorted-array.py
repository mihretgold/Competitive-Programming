class Solution:
    def search(self, nums: List[int], target: int) -> int:
        find = max(nums)
        length = len(nums)

        def bisect(arr, target, low, high):

            while low <= high:
                mid = low + (high - low)//2
               
                if nums[mid ] == target:
                    return mid
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            return -1

        idx = nums.index(find)
        idx1 = bisect(nums[:idx + 1], target, 0, idx)
        idx2 = bisect(nums[idx + 1:], target, idx + 1, length - 1)
        

        return max(idx1, idx2)
        