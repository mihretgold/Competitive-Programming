class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        storage = defaultdict(list)
        maxi = 0
        maxLength = 0
        
        def isPredecessor(word1, word2):
            i = 0
            j = 0
            count = 0
            
            while i < len(word1) and j < len(word2):
                if word1[i] == word2[j] or count == 0:
                    if  word1[i] != word2[j]:
                        count += 1
                        j += 1
                    else:                        
                        i += 1 
                        j += 1
                else:
                    return False
                
            return True
                
                
        
        for word in words:
            length = len(word)
            maxLength = max(maxLength, length)
            storage[length].append([word, 1])
            
        if maxLength > 0:
            maxi = 1
        
        # print(storage)
        for idx in range(2, maxLength + 1):
            if len(storage[idx-1]) == 0 or len(storage[idx]) == 0:
                continue
                
            for i, word2 in enumerate(storage[idx]):
                maxVal = 0
                for word1 in storage[idx-1]:
                    # print(word1[0], word2[0], isPredecessor(word1[0], word2[0]))
                    if isPredecessor(word1[0], word2[0]):
                        maxVal = max(maxVal, word1[1])
                        
                storage[idx][i][1] += maxVal
                # print(storage, storage[idx][i][1], maxVal)
                maxi = max(maxi, storage[idx][i][1])
                        
                    
        return maxi
                    
        
        