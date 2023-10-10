class Solution:
    def minOperations(self, nums: List[int]) -> int:
        mini = min(nums)
        length = len(nums)
        wantedNums = set(nums)
        ans = float('inf')
        count = 0
        nums = list(wantedNums)
        nums.sort()
        # print(nums)
        def binary(search, check):
            low = 0 
            high = len(nums) - 1
            
            while low <= high:
                mid = low + (high - low)//2
                
                if (check and nums[mid] < search) or (not check and nums[mid] <= search):
                    low = mid + 1
                else:
                    high = mid - 1
            # print(search, check, high, low)        
            if check:
                return high + 1
            else:
                return high
        
        for num in nums:
            count = binary(num, 1)
            count2 = binary(num + length - 1, 0)
            val = count2 - count + 1
            ans = min(ans, length - val)
                
        return ans
            
        
        