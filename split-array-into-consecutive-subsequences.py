class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        length = len(nums)
        heap = []
        heap2 = []
        mini = float('inf')
        popped = []
        check = True
        for i in range(length):
            if heap:
                print(nums[i], heap[0][0], heap2[0][1])
            if heap and  (nums[i] - heap[0][0] == 1 or nums[i] - heap2[0][1] == 1):
                # print(heap)
                # print(nums[i], heap[0][0], heap2[0][1])
                if nums[i] - heap[0][0] == 1:
                    # print(num, index)
                    num, index = heappop(heap)
                    heap2.remove((index, num))
                    heappush(heap, (nums[i], index+1))
                    heappush(heap2, (index+1, nums[i]))
                else:
                    index, num = heappop(heap2)
                    heap.remove((num, index))
                    heappush(heap, (nums[i], index+1))
                    heappush(heap2, (index+1, nums[i]))
            
            else:
                if heap and nums[i] > heap[0][0] and heap[0][1] >= 3:
                    num, index = heappop(heap)
                    heap2.remove((index, num))
                elif heap and nums[i] > heap[0][0] and heap[0][1] < 3:
                    return False
                heappush(heap, (nums[i], 1))
                heappush(heap2, (1, nums[i]))
        print(heap)
        for a, b in heap:
            if b < 3:
                check = False
                break 
            
           
            

        return check