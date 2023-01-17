class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        length = len(heights)
                 
        for i in range(length):
            mini = i
            for j in range(i+1, length):
                if heights[mini] < heights[j]:
                    mini = j
            heights[mini], heights[i] = heights[i], heights[mini]
            names[mini], names[i] = names[i], names[mini]
                                
        return names
        