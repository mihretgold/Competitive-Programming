class Solution:
    def minDeletions(self, s: str) -> int:
        lettersCount = Counter(s)
        storage = defaultdict(int)
       
        maxi = 0
        for letter in lettersCount:
            storage[lettersCount[letter]] += 1
            maxi = max(maxi, lettersCount[letter])
      
        answer = 0
    
        for num in range(maxi, 0, -1):
            count = storage[num] - 1
            
            if count > 0:
                answer += count
                if num > 1:
                    storage[num-1] += count
            
                    
                    
        return answer