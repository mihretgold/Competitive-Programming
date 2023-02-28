class Solution:
    '''
    1 1 2 6 24
    24 24 12 4 1
    4 12 24 24
    '''
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [1 for _ in range(length+1)]
        suffix = [1 for _ in range(length)]
        prefix = [1 for _ in range(length+1)]
        
        for index in range(length-2, -1 , -1):
            suffix[index] = suffix[index+1] * nums[index + 1]
        suffix.append(1)
        
        for index in range(1, length+1):
            prefix[index] = prefix[index-1] * nums[index-1]
        
        print(prefix)
        print(suffix)
        for index in range(length):
            print(prefix[index], suffix[index])
            answer[index] = prefix[index] * suffix[index]

        return answer[:-1]