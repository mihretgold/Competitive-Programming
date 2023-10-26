class Solution:
    #Given arr -> all unique, all > 1, each num can be used multiple x, each non leaf node must be product of it's childern  
    #Req: num of binary tree
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        seen = set(arr)
        length = len(arr)
        arr.sort()
        answer = 0
        dp = {x: 1 for x in arr}
        MOD = 10 ** 9 + 7

        for num1 in arr:
            for num2 in arr:
                if num2 > num1 ** 0.5:
                    break

                if num1 % num2 == 0 and num1//num2 in seen:
                    if num1 // num2 == num2:
                        dp[num1] += dp[num2] * dp[num2]
                    else:
                        dp[num1] += dp[num2] * dp[num1//num2] * 2

                    dp[num1] %= MOD

        answer = sum(dp.values()) % MOD
        return answer

        
        
    
            
        