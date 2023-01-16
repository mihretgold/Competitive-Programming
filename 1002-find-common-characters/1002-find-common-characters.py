class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        answer = []
        string = words[0]
        length = len(words)
        
        for index in range(1, length):
            length_words = len(words[index])
            temp = ''
            for letter in range(length_words):
                if words[index][letter] in string:
                    temp += words[index][letter]
                    string = string.replace(words[index][letter], "", 1)
            string = temp
        
        answer = list(string)
        
        return answer