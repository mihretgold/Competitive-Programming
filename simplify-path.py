class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        file = path.split("/")
        length = len(file)
        print(file)
        
        for index in range(length):
            if file[index] == '' or file[index] == '.':
                continue
            elif len(stack) != 0 and file[index] == "..":
                stack.pop()
            elif file[index] == "..":
                continue
            else:
                stack.append(file[index])

        answer = "/" + "/".join(stack)
        return answer