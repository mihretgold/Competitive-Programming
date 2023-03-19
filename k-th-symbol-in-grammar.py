class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def calVal(n, index, parity):
            if n <= 1:
                if parity == 0:
                    return 1
                else:
                    return 0
            temp = 1
            if index % 2 == 0:
                temp = 0
            
            val = calVal(n-1, ceil(index/2), temp)

            if val == 1:
                if parity == 0:
                    return 0
                else:
                    return 1
            if val == 0:
                if parity == 0:
                    return 1
                else:
                    return 0

        parity = 1
        if k % 2 == 0:
            parity = 0
        return calVal(n, ceil(k/2), parity)