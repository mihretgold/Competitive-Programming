class Solution:

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        map_order = {}
        length_order = len(order)
        length_words = len(words)
        
        for index in range(length_order):
            map_order[order[index]] = index
                        
        for  index in range(length_words - 1):
            word1 = words[index]
            word2 = words[index + 1]
            
            letter = 0
            while(letter < len(word1) and letter < len(word2)):
                if map_order[word1[letter]] > map_order[word2[letter]]:
                    return False
                elif map_order[word1[letter]] < map_order[word2[letter]]:
                    break
                letter += 1
            
            if letter == len(word2) and len(word1) > len(word2):
                return False
            
        return True
                
            