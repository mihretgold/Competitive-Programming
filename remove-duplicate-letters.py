class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        length = len(s)
        store_index = defaultdict(int)
        check = set()
        stack = []
        
        for index in range(length):
            store_index[s[index]] = index
            
        for index in range(length):
            if not stack or (s[index] not in check and s[stack[-1]] < s[index]) :
                stack.append(index)
                check.add(s[index])
            else:
                while stack and s[index] not in check and index < store_index[s[stack[-1]]] and s[stack[-1]] >= s[index]:
                    check.remove(s[stack[-1]])
                    stack.pop()
               
                if s[index] not in check:
                    print("hello", s[index])
                    check.add(s[index])
                    stack.append(index)
            print(stack)


            

        len_stack = len(stack)
        answer = ["" for _ in range(len_stack)]
        
        for index in range(len(stack)):
            answer[index] = s[stack[index]]
            
        return "".join(answer)