class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        length = len(arr)

        if arr[0] != 1:
            arr[0] = 1

        for i in range(1, length):
            if arr[i] != arr[i-1]:
                arr[i] = arr[i-1] + 1

        answer = max(arr)
        return answer