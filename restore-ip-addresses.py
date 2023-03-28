class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        def calcIpAddress(index, path):
            if index == len(s):
                if len(path) == 4:
                    result.append(".".join(path))
                    return

            for i in range(index, len(s)):
                val = s[index:i+1]
                if len(val) > 1 and val[0] == "0":
                    return
                if val.isdigit():
                    val = int(val)
                    if val <= 255 and val >= 0:
                        path.append(str(val))
                        calcIpAddress(i+1, path)
                        path.pop()

        calcIpAddress(0, [])

        return result