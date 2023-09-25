class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        mem = defaultdict(int)
        players = []
        length = len(scores)

        for index in range(length):
            players.append((ages[index], scores[index]))

        dp = [0]*length
        players.sort()
        maxScore = 0

        for row in range(length):
            maxi = 0
            for col in range(row):
                if players[row][0] != players[col][0] and players[col][1] > players[row][1]:
                    continue
                
                maxi = max(dp[col], maxi)
            dp[row] = maxi + players[row][1]
            maxScore = max(maxScore, dp[row])

        return maxScore