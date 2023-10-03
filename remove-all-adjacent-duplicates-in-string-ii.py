class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        store = defaultdict(int)

        stack = []

        for string in s:
            if stack and stack[-1][0] == string:
                stack[-1][1] += 1
            else:
                stack.append([string, 1])
           

            if stack[-1][1] == k:
                stack.pop()

        answer = ""
        
        for string, length in stack:
            for _ in range(length):
                answer += string

        return answer