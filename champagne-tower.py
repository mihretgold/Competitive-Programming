''' mem = default
def dp(row, col, poured):
    if row == query_row and col == query_glass:
        return poured

    if row >= query_row or col >= query_row:
        return 0
    if poured >= 1:
        poured -= 1
    else:
        poured = 0
    
    
    left = dp(row + 1, col, poured/2)
    right = dp(row + 1, col+1, poured/2)

    return left + right

return dp(0, 0, poured)'''
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = []
        for index in range(query_row+2):
            temp = []
            for j in range(index+1):
                temp.append(0)

            dp.append(temp)

        dp[0][0] = poured
        lengthRow = len(dp)
        for row in range(lengthRow):
            lengthCol = len(dp[row])
            for col in range(lengthCol):
                if row + 1 < lengthRow:
                    if dp[row][col] >= 1:
                        flow = dp[row][col] - 1
                        dp[row][col] -= flow
                        dp[row + 1][col] += flow/2
                        if col + 1 < len(dp[row+1]):
                            dp[row+1][col+1] += flow/2

       

        return dp[query_row][query_glass]