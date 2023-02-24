class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        counts = defaultdict(int)
        counts[0] = 1
        answer = 0
        length = len(nums)
        
        for index in range(length):
            prefix += nums[index]
            if prefix - k in counts:
                answer += counts[prefix-k]
            counts[prefix] += 1
            
        return answer
        