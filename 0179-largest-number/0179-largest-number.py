class Solution:
    def customComparator(self, a: str, b: str):
        ans = - 1
        if (a+b) < (b+a):
            ans = 1
        elif (a+b) == (b+a):
            ans = 0
        
        return ans
        
    def largestNumber(self, nums: List[int]) -> str:
        length = len(nums)
        list_string = []
        # count_zero = 0
        for num in nums:
            # if num == 0:
            #     count_zero += 1
            list_string.append(str(num))
            
        # if count_zero == length:
        #     return "0"
        
        sorted_list = sorted(list_string, key = cmp_to_key(self.customComparator));
        # list_string.sort(key = cmp_to_key(self.customComparator));
        
        String =str(int("".join(sorted_list)))
            
        return String
            
        