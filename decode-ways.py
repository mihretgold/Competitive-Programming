class Solution:
    def numDecodings(self, s: str) -> int:
        mem = defaultdict(int)
        def calc(s):
            if s not in mem:
                if s == "":
                    return 1

                count = 0
                if s[0] != "0":
                    count += calc(s[1:])
                if s[0] != '0' and len(s) > 1:
                    if 1 <= int(s[:2]) <= 26:
                        count += calc(s[2:])

                mem[s] = count

            return mem[s]
        return calc(s)