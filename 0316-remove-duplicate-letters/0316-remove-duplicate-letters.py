class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        visted = set()
        lastIndex = defaultdict(int)
        length = len(s)
        
        for index in range(length):
            lastIndex[s[index]] = index
            
        stack = []
        
        for index, letter in enumerate(s):
            if not stack or s[stack[-1]] < letter and letter not in visted:
                visted.add(letter)
                stack.append(index)
                # print(1, letter, stack, visted)
            else:
                while stack and letter not in visted and index < lastIndex[s[stack[-1]]] and s[stack[-1]] >= s[index]:
                    
                    val = stack.pop()
                    visted.remove(s[val])
                    
                if letter not in visted:
                    stack.append(index)
                    visted.add(letter)
                # print(2, letter, stack, visted)
        
        answer = ""
        
        for num in stack:
            answer += s[num]
            
        return answer
                
                
        
        