class Solution:
    # count sorting
    def findKthLargest(self, nums: List[int], k: int) -> int:
        rangesPos = max(nums)
        rangesNeg = abs(min(nums))
        countPos = [0 for _ in range(rangesPos+1)]
        countNeg = [0 for _ in range(rangesNeg+1)]
        positive = []
        negative = []
        for num in nums:
            if num >= 0:
                countPos[num] += 1
            else:
                countNeg[-num] += 1
        for i, num in enumerate(countPos):
            for _ in range(num):
                positive.append(i)
        for i in range(len(countNeg)-1, -1, -1):
            for _ in range(countNeg[i]):
                negative.append(-i)

        answer = negative + positive 

        return answer[-k]