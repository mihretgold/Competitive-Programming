class Solution:
    def printVertically(self, s: str) -> List[str]:
        maxi = 0
        list_s = list(s.split())
        length_row = len(list_s)
        answer = []
        
        #iterate through the string and find max string length
        for index in range(length_row):
            maxi = max(maxi, len(list_s[index]))
        
        #append space for all the strings less than the max length
        for col in range(length_row):
            length_word = len(list_s[col])
            for row in range(length_word, maxi):
                list_s[col] += ' '
        
        #Append each letters by column
        for col in range(maxi):
            temp = ''
            for row in range(length_row):
                temp += list_s[row][col]
            answer.append(temp)
        
        length_col = len(answer)
        length_answer = len(answer[0])            
        #Remove trailing spaces
        for col in range(length_col):
            for row in range(length_answer-1, -1, -1):
                if answer[col][row] != ' ':
                    answer[col] = answer[col][:row+1]
                    break
        
        return answer
        