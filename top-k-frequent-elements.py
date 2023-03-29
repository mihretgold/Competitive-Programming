class Solution:
    def quickSort(self, arr):
        length = len(arr)        
        if length <= 1:
            return arr

        m = length//2
        pivot = arr[random.randint(0, length-1)][0]
        left = []
        right = []
        mid = []

        for num in arr:
            if num[0] < pivot:
                left.append(num)
            elif num[0] > pivot:
                right.append(num)
            else:
                mid.append(num)


        return self.quickSort(right) + mid + self.quickSort(left)

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       count = Counter(nums)
       store = []
       for num in count:
           store.append([count[num], num])

       store = self.quickSort(store)
       answer = []

       for index in range(k):
           answer.append(store[index][1])

       return answer