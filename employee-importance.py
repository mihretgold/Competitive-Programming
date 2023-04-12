"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict(list)
        important = defaultdict(int)

        for employee in employees:
            graph[employee.id] = employee.subordinates

        for employee in employees:
            important[employee.id] = employee.importance

        result = 0
        visted = set()
        
        def dfs(person):
            nonlocal result
            result += important[person]
            visted.add(person)

            for sub in graph[person]:
                if sub not in visted:
                    dfs(sub)

        dfs(id)

        return result