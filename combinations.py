class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        path = []
        def calcCombine(index, path):
            if len(path) == k:
                combinations.append(path[:])
                return

            if index > n: 
                return

            path.append(index)
            calcCombine(index+1,path)
            path.pop()
            calcCombine(index+1,path)

        calcCombine(1, path)
        return combinations