class Solution:
    '''
    Algorithm
    s1.change str in to list
    s2. if chr is G add G to string word if) check if the next index is last index was ( or l 
    '''
    def interpret(self, command: str) -> str:
        word = ""
        comand_list=list(command)
        length= len(comand_list)
        for index in range(length):
            if comand_list[index] == 'G':
                word += comand_list[index]
            elif comand_list[index] == ')' and comand_list[index-1] == '(':
                word += 'o'
            elif comand_list[index] == ')' and comand_list[index-1] == 'l':
                word += 'al'
                 
        return word