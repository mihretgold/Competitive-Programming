class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = 0
        count = defaultdict(int)
        count[0] = 1
        answer = 0
        
        for num in nums:
            prefix += num
            if prefix % k in count:
                answer += count[prefix % k]
            count[prefix%k] += 1
            
        return answer
                
            