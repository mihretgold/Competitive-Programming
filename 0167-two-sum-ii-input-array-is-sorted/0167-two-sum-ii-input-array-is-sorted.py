class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        complement = set()
        ans = []
        length = len(numbers)
        for num in range(length):
            check = target - numbers[num]
            if check in complement:
                a = numbers.index(check) + 1
                if a < num + 1:
                    ans = [a, num+1]
                    break
                else:
                    ans = [num+1, a]
                    break
            else:
                complement.add(numbers[num])
        
        return ans
                
                
        