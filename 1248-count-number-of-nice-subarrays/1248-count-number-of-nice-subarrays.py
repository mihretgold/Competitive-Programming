class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        length = len(nums)
        check = defaultdict(int)
        check[0] = 1
        
        for index in range(length):
            if nums[index] % 2 == 0:
                nums[index] = 0
            else:
                nums[index] = 1
        
        count = 0
        sums = 0
        for num in nums:
            sums += num
            if sums - k in check:
                count += check[sums - k]
            check[sums] += 1
            
                
                
        return count