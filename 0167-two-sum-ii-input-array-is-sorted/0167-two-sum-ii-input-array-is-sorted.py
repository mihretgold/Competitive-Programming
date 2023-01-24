class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        start = 0
        end = length - 1
        ans = []
        while(start < end):
            if numbers[start] + numbers[end] == target:
                ans = [start+1, end+1]
                break
            elif numbers[start] + numbers[end] > target:
                end -= 1
            else:
                start += 1
                
        return ans