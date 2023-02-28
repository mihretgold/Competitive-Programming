class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        length = len(s)
        stack = []
        count = 0
           
        for index in range(length):
            if len(stack) != 0  and stack[-1] == "(" and s[index] == ")":
                stack.pop()
                stack.append("1")
            elif len(stack) != 0  and stack[-1].isdigit() and s[index] == ")":
                score = 0
                while stack[-1].isdigit():
                    score += int(stack[-1])
                    stack.pop()
                if stack[-1] == "(":
                    stack.pop()
                    stack.append(str(2*score))
                    score = 0
            else:
                stack.append(s[index])
                score = 0
        
        print(stack)
        stack = list(map(int, stack)) 
        count = sum(stack)

        return count