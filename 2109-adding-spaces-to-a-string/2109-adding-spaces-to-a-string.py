class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        answer = ''
        index_space = 0
        index_string = 0
        length_space = len(spaces)
        length_string = len(s)
        while index_string < length_string:
            if index_space < length_space and index_string == spaces[index_space]:
                answer += ' '
                answer += s[index_string]
                index_space += 1
            else:
                answer += s[index_string] 
            index_string += 1
        
        return answer