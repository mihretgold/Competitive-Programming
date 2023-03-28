class Solution:
    def __init__(self):
        self.count = 0

    def mergeSort(self, arr, low, high, diff):
        if low == high:
            return [arr[low]]
        
        mid = low + (high - low)//2
        left = self.mergeSort(arr, low, mid, diff)
        right = self.mergeSort(arr, mid + 1, high, diff)

        return self.merge(left, right, diff)

    def merge(self, left, right, diff):
        lengthL = len(left)
        lengthR = len(right)
        i = 0
        j = 0

        while i < lengthL and j < lengthR:
            if (left[i][0] - right[j][0]) <= (left[i][1] - right[j][1] + diff):
                self.count += (lengthR - j)
                i += 1
            else:
                j += 1

        leftPtr = 0
        rightPtr = 0
        answer = []

        while leftPtr < lengthL or rightPtr < lengthR:
            if rightPtr == lengthR or (leftPtr < lengthL and (left[leftPtr][0] - left[leftPtr][1]) < (right[rightPtr][0] - right[rightPtr][1])):
                answer.append(left[leftPtr])
                leftPtr += 1
            else:
                answer.append(right[rightPtr])
                rightPtr += 1

        return answer


    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        nums = list(zip(nums1, nums2))
        self.mergeSort(nums, 0, len(nums)-1, diff)
        return self.count