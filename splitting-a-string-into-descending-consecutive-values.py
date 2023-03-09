class Solution:
    def splitString(self, s: str) -> bool:
        current = []
        def calcValid(index):
            if index >= len(s):
                return len(current) >= 2

            for i in range(index, len(s)):
                val = int(s[index:i+1])
                if not current or val == current[-1] - 1:
                    current.append(val)
                    if calcValid(i+1):
                        return True

                    current.pop()
            
            return False

        return calcValid(0)