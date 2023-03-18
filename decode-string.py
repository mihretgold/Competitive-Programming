class Solution:
    '''
    Algo
    1) initialize stack
    2) append until u get to a closed bracket
    3) then pop until top is not digit or stack is empty
    4) then push back the conctenated string
    5) return the joined stack
    '''
    def decodeString(self, s: str) -> str:
        stack = []
        length = len(s)
        digit = False
        for char in s:
            if char == "]":
                # use list
                string = []
                num = ""
                while stack and stack[-1] != "[":
                    string.append(stack.pop())
                stack.pop()
                while stack and stack[-1].isdigit():
                    num += stack[-1]
                    stack.pop()
                string = string[::-1]
                ans = []
                num = num[::-1]
                size = int(num)
                ans = string * size
                stack+=ans
            else:
                stack.append(char) 

        if stack and stack[-1].isdigit():
            return ""
                

        return "".join(stack)