class Solution:
    def minTimeToType(self, word: str) -> int:
        answer = 0
        start = 1

        for letter in word:
            ascii = ord(letter) - ord('a') + 1
            if ascii == start:
                answer += 1
                continue

            val1 = abs(start - ascii)
            if start <= ascii:
                val2 = (start - 1) + (26 - ascii) + 1
            else:
                val2 = (ascii - 1) + (26 - start) + 1

            answer += min(val1, val2) + 1
            # print(val1, val2, answer)
            start = ascii

        return answer

        