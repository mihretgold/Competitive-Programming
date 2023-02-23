class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxi = 0
        fruits_dict = defaultdict(int)
        start = 0
        length = len(fruits)
        for end in range(length):
            fruits_dict[fruits[end]] += 1           
            while len(fruits_dict) > 2:
                fruits_dict[fruits[start]] -= 1
                if fruits_dict[fruits[start]]  == 0:
                    fruits_dict.pop(fruits[start])
                start += 1
            maxi = max(maxi, end - start + 1)  
            
        return maxi
                