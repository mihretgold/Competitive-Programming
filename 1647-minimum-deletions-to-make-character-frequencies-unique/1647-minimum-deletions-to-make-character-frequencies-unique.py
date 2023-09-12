class Solution:
    def minDeletions(self, s: str) -> int:
        lettersCount = Counter(s)
        storage = defaultdict(int)
        # print(lettersCount)
        maxi = 0
        for letter in lettersCount:
            storage[lettersCount[letter]] += 1
            maxi = max(maxi, lettersCount[letter])
        # print(storage)
        answer = 0
        # print(maxi)
        for num in range(maxi, 0, -1):
            count = storage[num] - 1
            # print(count, storage[num])
            if count > 0:
                answer += count
                if num > 1:
                    storage[num-1] += count
            
                    
                    
        return answer