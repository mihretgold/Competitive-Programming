class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        wordsCount = 0
        count = 0
        length = len(words)
        answer = []
        left = 0

        for i in range(length):
            lastWord = len(words[i])
            wordsCount += lastWord
           
            if wordsCount + (i - left) > maxWidth:
                wordsCount -= lastWord
                
                space = (maxWidth - wordsCount)//max((count - 1), 1)
                remainder = (maxWidth - wordsCount) % max((count - 1), 1)
               
                string = ""
                spaceString = " " * space
                for j in range(left, i - 1):
                    if remainder:
                        string += words[j] + spaceString + " "
                        remainder -= 1
                    else:
                        string += words[j] + spaceString
                if string == "":
                    string += words[i - 1] + spaceString
                else:
                    string += words[i - 1]

                answer.append(string)

                wordsCount = lastWord
                if i == length - 1:
                    string = words[i] + " "*(maxWidth - lastWord) 
                    answer.append(string)
                left = i
                count = 0
            elif i == length - 1:
                string = ""
                for j in range(left, i + 1):
                    string += words[j] + " "

                string = string[:-1]
                string += " " * (maxWidth - len(string)) 
                answer.append(string)
            count += 1
   

        return answer


        