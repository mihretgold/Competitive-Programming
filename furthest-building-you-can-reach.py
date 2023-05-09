class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        length = len(heights)
        heap = []

        for index in range(1, length):
            diffrence = heights[index] - heights[index-1]
            if diffrence <= 0:
                continue
            if (bricks == 0 or diffrence > bricks) and ladders == 0:
                return index - 1
            elif diffrence <= bricks:
                bricks -= diffrence
                heappush(heap, -diffrence)
            elif (not heap or (heap and -diffrence <= heap[0])) and ladders > 0:
                ladders -= 1
                continue
            elif heap and -diffrence > heap[0] and ladders > 0:
                maxi = heappop(heap)
                bricks += (-maxi - diffrence)
                heappush(heap, -diffrence)
                ladders -= 1

        return length-1