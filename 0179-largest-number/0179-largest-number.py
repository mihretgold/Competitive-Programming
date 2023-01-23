class Solution:
    def customComparator(self, a: str, b: str):
        if (a+b) < (b+a):
            return 1
        elif (a+b) == (b+a):
            return 0
        else:
            return -1
        
    def largestNumber(self, nums: List[int]) -> str:
        length = len(nums)
        list_string = []
        count_zero = 0
        for num in nums:
            if num == 0:
                count_zero += 1
            list_string.append(str(num))
            
        if count_zero == length:
            return "0"
        
        sorted_list = sorted(list_string, key = cmp_to_key(self.customComparator));
        # list_string.sort(key = cmp_to_key(self.customComparator));
        
        String = "".join(sorted_list)
            
        return String
            
        