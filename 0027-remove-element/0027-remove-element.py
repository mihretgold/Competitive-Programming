class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for number in nums:
            if number != val:
                nums[count] = number
                count += 1
        return count