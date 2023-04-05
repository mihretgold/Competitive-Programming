class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        length = len(nums)
        count = 0

        for index in range(length):
            gcd = nums[index]
            for num in range(index, length):
                gcd = math.gcd(gcd,nums[num])
                if gcd == k:
                    count += 1
                elif gcd < k:
                    break

        return count