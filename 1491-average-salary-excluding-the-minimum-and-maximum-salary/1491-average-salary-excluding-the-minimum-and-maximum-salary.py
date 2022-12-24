class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        print(salary)
        end = len(salary) - 1
        sums = 0
        count = 0
        for index in range(1,end):
            sums += salary[index]
            index += 1
            count += 1
        average = sums/count
        return average