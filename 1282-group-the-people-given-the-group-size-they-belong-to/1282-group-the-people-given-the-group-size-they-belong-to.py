class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        storage = defaultdict(list)
        answer = []
        
        for index, value in enumerate(groupSizes):
            storage[value].append(index)
            if len(storage[value]) == value:
                answer.append(storage[value])
                storage[value] = []
                
        return answer
        
        
        