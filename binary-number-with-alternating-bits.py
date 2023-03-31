class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        check = True
        val = 0
        if n & 1 != 0:
            val = 1

        for index in range(1, n.bit_length()):

            if val == 1 and n & 1<<index == 0:
                val = 0
                check = True
            elif val == 0 and n & 1<<index != 0:
                val = 1
                check = True
            else:
                check = False
                break


        return check