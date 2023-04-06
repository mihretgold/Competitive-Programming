class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        maxi = max(nums)
        mini = min(nums)
        maxi = max(maxi.bit_length(), mini.bit_length())
        lengthBit = maxi.bit_length()
        answer = 0
        length = len(nums)
        count = 0

        for index in range(len(nums)):
            if nums[index] < 0:
                nums[index] = - nums[index]
                count += 1

        for bit in range(maxi):
            total = 0
            for index in range(length):
                total += nums[index] & int(1 << bit)          
            
            if total % 3 != 0:
                answer |= 1<<bit

        if count % 3 != 0:
            answer = -answer

        return answer