class Solution:
    def __init__(self):
        self.count = 0

    def mergeSort(self, arr, low, high):
        if low == high:
            return [arr[low]]

        mid = low + (high-low)//2
        left = self.mergeSort(arr, low, mid)
        right = self.mergeSort(arr, mid+1, high)

        return self.merge(left, right)

    def merge(self, left, right):
        lengthL = len(left)
        lengthR = len(right)
        checkPtrL = lengthL - 1
        checkPtrR = lengthR - 1

        while checkPtrL >= 0 and checkPtrR >= 0:
            if left[checkPtrL] > 2*right[checkPtrR]:
                self.count += (checkPtrR + 1)
                checkPtrL -= 1
            else:
                checkPtrR -= 1



        i = 0
        j = 0
        answer = []
        while i < lengthL or j < lengthR:
            if j == lengthR or(i < lengthL and left[i] < right[j]):
                answer.append(left[i])
                i += 1
            else:
                answer.append(right[j])
                j += 1

        return answer

    def reversePairs(self, nums: List[int]) -> int:
        self.mergeSort(nums, 0, len(nums)-1)
        return self.count