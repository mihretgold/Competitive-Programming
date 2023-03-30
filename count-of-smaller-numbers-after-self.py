class Solution:
    def mergeSort(self, nums: List[int], low:int, high:int) -> List[int]:
        if low == high:
            return [nums[low]]

        mid = low + (high - low)//2
        left = self.mergeSort(nums, low, mid)
        right = self.mergeSort(nums, mid+1, high)

        return self.merge(left, right)

    def merge(self, left: List[int], right: List[int]) -> List[int]:
        i = 0
        j = 0
        lengthL = len(left)
        lengthR = len(right)
        result = []

        
        while i < lengthL and j < lengthR:
            if right[j][0] < left[i][0]:   
                result.append(right[j])
                j += 1
            else:
                self.answer[left[i][1]] += j
                result.append(left[i])
                i += 1
        

        while i < lengthL:
            self.answer[left[i][1]] += lengthR
            result.append(left[i])
            i += 1

        while j < lengthR:
            result.append(right[j])
            j += 1

        return result

    def countSmaller(self, nums: List[int]) -> List[int]:
        arr = []
        length = len(nums)
        for i in range(length):
            arr.append([nums[i], i])
        self.answer = [0 for _ in range(length)]
        self.mergeSort(arr, 0, length-1)
        

        return self.answer