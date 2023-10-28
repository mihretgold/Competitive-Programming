class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = [[0 for _ in range(5)] for _ in range(n)]
        MOD = (10 ** 9) + 7
        graph = defaultdict(int)
        graph[0] = [1]
        graph[1] = [0, 2]
        graph[2] = [0,1,3,4]
        graph[3] = [2, 4]
        graph[4] = [0]
        
        for index in range(5):
            dp[0][index] = 1
            
        for index in range(n-1):
            for idx in range(5):
                for child in graph[idx]:
                    dp[index + 1][child] += dp[index][idx]
            
        # print(dp[n-1])
        answer = sum(dp[n-1]) % MOD
        
        return answer