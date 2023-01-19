class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        length = len(heights)
                 
        for i in range(1, length):
            key_h = heights[i]
            key_n = names[i]
            j = i - 1
            while j>=0 and key_h > heights[j]:
                heights[j+1] = heights[j]
                names[j+1] = names[j]
                j -= 1
            heights[j+1] = key_h
            names[j+1] = key_n
            
                                
        return names
        