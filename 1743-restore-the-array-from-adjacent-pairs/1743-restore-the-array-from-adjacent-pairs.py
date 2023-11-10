class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for pair1, pair2 in adjacentPairs:
            graph[pair1].append(pair2)
            graph[pair2].append(pair1)
            
        start = - 1
            
        for num in graph:
            if len(graph[num]) == 1:
                start = num
                break
                
        stack = [start]
        answer = [start]
        visted = set()
        visted.add(start)
        
        while stack:
            node = stack.pop()
            
            for child in graph[node]:
                if child not in visted:
                    stack.append(child)
                    answer.append(child)
                    visted.add(child)
                    
        return answer
            