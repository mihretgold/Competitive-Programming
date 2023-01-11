class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        map_files = defaultdict(list)
        for string in paths:
            list_string = string.split(' ')
            length = len(list_string)
            root = list_string[0]
            
            for word in range(1, length):
                first = list_string[word].index('(')
                last = list_string[word].index(')')
                key = list_string[word][first+1:last]
                value = list_string[word][:first]
                ans = root + "/" + value
                map_files[key].append(ans)                    
                   
        answer = []          
        for word in map_files.values():
            length_values = len(word)
            if length_values > 1:
                answer.append(word)
        
        return answer 
                    
                
                
            