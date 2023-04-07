class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        answer = []
        found = set()
        for a, b in edges:
            found.add(b)

        for index in range(n):
            if index not in found:
                answer.append(index)

        return answer