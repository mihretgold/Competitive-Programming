class Solution:

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        map_order = {}
        for index, letter in enumerate(order):
            map_order[letter] = index
        
        length = len(words)
       
        for index in range(length -1):
            word1 = words[index]
            word2 = words[index + 1]
            i = 0 
            len_w1 = len(word1)
            len_w2 = len(word2)
            while i < len_w1 and i < len_w2:
                if map_order[word1[i]] > map_order[word2[i]]:
                    return False
                elif map_order[word1[i]] < map_order[word2[i]]:
                    break
                i += 1  
                
            if i == len_w2 and len_w1 > len_w2:
                return False
                
        
        return True
        
                    
                
            