class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        answer = []
        check = len(nums)//3
        
        for num in counter:
            if counter[num] > check:
                answer.append(num)
                
        return answer
        