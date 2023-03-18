class Solution:
    # [(1,2), (2, 1), (3, 0)]

    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        answer = []
        startCheck = []

        for index in range(len(intervals)):
            startCheck.append((intervals[index][0], index))
        startCheck.sort()

        for a, b in intervals:
            low = 0
            high = len(intervals) - 1
            while low <= high:
                mid = low + (high - low)//2
                if startCheck[mid][0] >= b:
                    high = mid - 1
                else:
                    low = mid + 1
            if low != len(intervals):
                answer.append(startCheck[low][1])
            else:
                answer.append(-1)

        return answer