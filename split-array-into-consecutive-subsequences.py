class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        length = len(nums)
        heap = [(nums[0], 1)]
        check = True
        for i in range(1, length):
            if nums[i] - heap[0][0] == 1:
                num, index = heappop(heap)
                heappush(heap, (nums[i], index+1))  
            elif nums[i] == heap[0][0]:
                heappush(heap, (nums[i], 1))         
            else:
                found = False
                while heap and not found:
                    num, index = heappop(heap)
                    if nums[i] - num == 1:
                        heappush(heap, (nums[i], index+1))
                        found = True
                    elif index < 3:
                        check = False

                if not found:
                    heappush(heap, (nums[i], 1))
        
        for a, b in heap:
            if b < 3:
                check = False
                break         

        return check