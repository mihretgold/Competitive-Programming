class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = [[0 for _ in range(26)] for _ in range(26)]
        answer = 0

        for word in words:
            i = ord(word[0]) - ord('a')
            j = ord(word[1]) - ord('a')

            if count[j][i]:
                answer += 4
                count[j][i] -= 1
            else:
                count[i][j] += 1

        for idx in range(26):
            if count[idx][idx]:
                answer += 2
                break

        return answer