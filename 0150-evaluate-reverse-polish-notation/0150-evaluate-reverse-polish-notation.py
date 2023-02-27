class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        length = len(tokens)
        stack = []
        
        for index in range(length):
            if tokens[index] == "+" or tokens[index] == "-" or tokens[index] == "/" or tokens[index] == "*":
                a = int(stack[-1])
                stack.pop()
                b = int(stack[-1])
                stack.pop()
                if tokens[index] == "+":
                    ans = b + a
                    stack.append(ans)
                elif tokens[index] == "-":
                    ans = b - a
                    stack.append(ans)
                elif tokens[index] == "*":
                    ans = b * a
                    stack.append(ans)
                else:
                    ans = b / a
                    stack.append(ans)
            else:
                stack.append(tokens[index])
            
             
        return int(stack[-1])