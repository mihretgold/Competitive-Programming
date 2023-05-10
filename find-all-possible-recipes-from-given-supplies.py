class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        length = len(recipes)
        answer = []
        graph = defaultdict(list)
        indegree = defaultdict(int)

        queue = deque(supplies)
        for recipie in range(length):
            size = len(ingredients[recipie])
            for index in range(size):
                graph[ingredients[recipie][index]].append(recipes[recipie])
                indegree[recipes[recipie]] += 1
        supplies = set(supplies)
            

        while queue:
            food= queue.popleft()
            if food not in supplies:
                answer.append(food)

            for ingridient in graph[food]:
                indegree[ingridient] -= 1
                if indegree[ingridient] == 0:
                    queue.append(ingridient)

        return answer