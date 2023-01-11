class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        string = '\n'.join(source)
        length = len(string)
        answer = []
        index = 0
        word = ''
        while index < length:
            if index < length-1 and string[index] == '/' and string[index+1] == '/':
                while index < length and string[index] != '\n':
                    index += 1
            elif index < length-1 and string[index] == '/' and string[index+1] == '*':
                index += 2
                while index < length-1:
                    if string[index] == '*' and string[index+1] == '/':
                        break
                    index += 1
                index += 2
            else:
                if index < length:
                    word += string[index]
                index += 1
                
        length_word = len(word)
        letter = 0
        
        while letter < length_word:
            res = ""
            while letter < length_word and word[letter] != "\n":
                res += word[letter]
                letter += 1
                
            if len(res) != 0:
                answer.append(res)
            letter += 1
            
        return answer
        
                
            