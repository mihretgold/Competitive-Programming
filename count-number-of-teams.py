class Solution:
    def numTeams(self, rating: List[int]) -> int:
        soliders = []

        for index, rate in enumerate(rating):
            soliders.append((rate, index))

        soliders.sort()

        length = len(rating)
        dp = [0] * length
        answer = 0

        for idx in range(length-2, -1, -1):
            for j in range(idx + 1, length):
                if soliders[j][1] > soliders[idx][1]:
                    # print(soliders[j][])
                    dp[idx] += 1

        for idx in range(length-2, -1, -1):
            for j in range(idx + 1, length):
                if soliders[j][1] > soliders[idx][1]:
                    answer += dp[j]

        # for idx in range(length-2, -1, -1):
        soliders.reverse()
        dp = [0] * length

        for idx in range(length-2, -1, -1):
            for j in range(idx + 1, length):
                if soliders[j][1] > soliders[idx][1]:
                    dp[idx] += 1

        for idx in range(length-2, -1, -1):
            for j in range(idx + 1, length):
                if soliders[j][1] > soliders[idx][1]:
                    answer += dp[j]

        # print(dp)


        return answer