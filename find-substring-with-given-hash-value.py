class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        arr = [1]
        length = len(s)
        cache = {c:ord(c)-96 for c in 'abcdefghijklmnopqrstuvwxyz'}

        for idx in range(length):
            arr.append(arr[-1] * power)

        total = 0
        for idx in range(k):
            val = cache[s[idx]]
            total += (val * arr[idx])
           

        
        start = 0
        
        for index in range(k, length):
            if total % modulo == hashValue:
                return s[start:index]

            valEnd = cache[s[index]]
            valStart = cache[s[start]]
            total -= valStart 
            total //= power
            
            total += (valEnd * arr[k-1]) 
            start += 1

        
        if total % modulo == hashValue:
            return s[start:]

        return s