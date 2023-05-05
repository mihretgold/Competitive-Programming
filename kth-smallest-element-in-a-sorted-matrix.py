class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int: 
        heap = []
        length = len(matrix)
        length_col = len(matrix[0])

        for i in range(length):
            if matrix[i]:
                heappush(heap, (matrix[i][0], i, 0))

        index = 0
        while heap:
            index += 1
            num, row, col = heappop(heap)
            if col+1 < length_col:
                heappush(heap, (matrix[row][col+1], row, col+1))
            if index >= k-1:
                break

        if index == k:
            return matrix[0][0]
        if not heap:
            return 0
        
        return heap[0][0]