class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        prev = self.getRow(rowIndex-1)
        curr = [1 for _ in range(rowIndex+1)]
        for index in range(1, rowIndex):
            curr[index] = prev[index] + prev[index-1]

        return curr