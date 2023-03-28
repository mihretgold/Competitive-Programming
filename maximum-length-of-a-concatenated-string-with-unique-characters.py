class Solution:
    def maxLength(self, arr: List[str]) -> int:
        length = 0
        def calcMaxLength(index, path):
            nonlocal length
            if path:
                string = "".join(path)
                length = max(length, len(string))

            if index == len(arr):
                return 

            for i in range(index, len(arr)):
                if len(set(arr[i])) == len(arr[i]):
                    string = "".join(path) 
                    val = string + arr[i]
                    if not path or len(set(val)) == len(val):
                        path.append(arr[i])
                        calcMaxLength(i+1, path)
                        path.pop()

        calcMaxLength(0, [])

        return length