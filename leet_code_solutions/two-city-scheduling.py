class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        length = len(costs)
        arr = []
        sums = 0
        for index in range(length):
            diff = costs[index][0] - costs[index][1]
            arr.append((diff, costs[index][0], costs[index][1]))

        arr.sort()
        start = 0
        end = length - 1
        while start < end:
            sums += arr[start][1]
            sums += arr[end][2]
            start += 1
            end -= 1

        return sums