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
                if len(word) > 0:
                    answer.append(word)
                    word = ""
                index += 1
            elif index < length-1 and string[index] == '/' and string[index+1] == '*':
                index += 2
                while index < length-1:
                    if string[index] == '*' and string[index+1] == '/':
                        break
                    index += 1
                index += 2
            else:
                if  index == length -1:
                    word += string[index]
                    answer.append(word)
                    
                    # print(answer)
                elif string[index] == '\n' and len(word) > 0:
                    answer.append(word)
                    word = ''
                    # print(answer)
                elif index < length-2 and string[index + 1] == '/' and (string[index+2] == '*' or string[index+1] == '/') :
                    word += string[index]
                else:
                    if string[index] != '\n':
                        word += string[index]
                index += 1
                   
            
        return answer
        
                
            