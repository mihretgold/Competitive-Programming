class Solution:
    def candy(self, ratings: List[int]) -> int:
        length = len(ratings)
        ans = [0]*length
        rate = []

        for index, num in enumerate(ratings):
            rate.append((num, index))

        rate.sort()
        for num, index in rate:
            left = 0
            right = 0

            if (index - 1) >= 0:
                if ratings[index] != ratings[index-1]:
                    left = ans[index-1]
            if (index + 1) < length:
                if ratings[index] != ratings[index+1]:
                    right = ans[index+1]

            maxi = max(left, right)
            ans[index] = maxi + 1

        candies = sum(ans)

        return candies