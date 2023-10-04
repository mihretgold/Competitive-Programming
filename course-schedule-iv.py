class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        matrix = [[float('inf') for _ in range(numCourses)] for _ in range(numCourses)]
        answer = []

        for a, b in prerequisites:
            matrix[a][b] = 1

        for index in range(numCourses):
            matrix[index][index] = 0

        for k in range(numCourses):
            for row in range(numCourses):
                for col in range(numCourses):
                    newDistance = matrix[row][k] + matrix[k][col]
                    if newDistance < matrix[row][col]:
                        matrix[row][col] = newDistance

        for a, b in queries:
            value = matrix[a][b]
            answer.append(value != float('inf'))

        return answer