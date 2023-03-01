class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        length = len(arr)
        sums = 0
        index = 0
        while index < length:
            while stack and arr[stack[-1]] > arr[index]:
                top = stack[-1]
                right = index - top
                left = 0
                stack.pop()
                if stack:
                    left = top - stack[-1]
                else:
                    left = top + 1
                sums += arr[top]*right*left

            stack.append(index)      
            index += 1
        while stack:
            top = stack[-1]
            right = index - top
            left = 0
            stack.pop()
            if stack:
                left = top - stack[-1]
            else:
                left = top + 1
            sums += arr[top]*right*left

        
        return sums % (10**9 + 7)