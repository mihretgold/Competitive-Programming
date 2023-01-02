class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        sum = 0
        #Calculate sum before changes
        for num in nums:
            if num % 2 == 0:
                sum += num 
                
        for val in queries:
            #if new value being replaced is even we subtract it
            if nums[val[1]] % 2 == 0:
                sum -= nums[val[1]]
            nums[val[1]] = nums[val[1]] + val[0]
            #if new value being replaced is even we add it
            if nums[val[1]] % 2 == 0:
                sum += nums[val[1]]
            answer.append(sum)
        
        return answer