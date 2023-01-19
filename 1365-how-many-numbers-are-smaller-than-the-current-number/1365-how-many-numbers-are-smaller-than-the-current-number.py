class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = []
        map_num = {}
        sorted_num = sorted(nums)
        for index, num in enumerate(sorted_num):
            if num not in map_num:
                map_num[num] = index
        
        for num in nums:
            smaller_count = map_num[num]
            answer.append(smaller_count)
            
        return answer