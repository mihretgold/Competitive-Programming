class Solution:
    #Algo
    #1) get all index which are vowels 
    #2) get all vowels and sort based on ascii val
    #3) in order put sorted vowels in the index
    def sortVowels(self, s: str) -> str:
        length = len(s)
        vowelAscii = []
        answer = []
        vowels = {'a', 'A', 'e', 'E', 'i', "I", "o", "O", 'u', "U"}
        
        for index in range(length):
            if s[index] in vowels:
                vowelAscii.append((ord(s[index]), index))
        
        answer = list(s)
                
        vowelAscii.sort()
        answer = ""
        i = 0
        for index in range(length):
            if s[index] in vowels:
                answer += s[vowelAscii[i][1]]
                i += 1
            else:
                answer += s[index]
                
        return answer
            
        
        