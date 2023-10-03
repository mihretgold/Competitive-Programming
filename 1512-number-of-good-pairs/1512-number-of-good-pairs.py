class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        store = defaultdict(int)
        answer = 0
        
        for num in nums:
            if num in store:
                answer += store[num]           
            
            store[num] += 1
        
        return answer