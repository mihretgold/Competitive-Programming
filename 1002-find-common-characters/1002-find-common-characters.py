class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        lengthList = len(words)
        list_check = list(words[0])
        list_check.sort()
        answer = []
        
        for index in range(1, lengthList):
            list_word = list(words[index])
            list_word.sort()
            temp = ''
            length_ans = len(list_check)
            length_word = len(list_word)
            i = 0
            j = 0
            while i < length_ans and j < length_word:
                if list_word[j] == list_check[i]:
                    temp += list_word[j]
                    i += 1
                    j +=1
                elif list_word[j] < list_check[i]:
                    j += 1
                elif list_word[j] > list_check[i]:
                    i += 1 
            list_check = list(temp)
            
        for letter in list_check:
            answer.append(letter)
        
        return answer