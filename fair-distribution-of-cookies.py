class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        arr = [0]*k
        self.minimumUnfairness = float('inf')
        cookies.sort(reverse = True)
        def calcMin(index, arr):
            if index >= len(cookies):
                self.minimumUnfairness = min(self.minimumUnfairness, max(arr))
                return

            if max(arr) >= self.minimumUnfairness:
                return

            for i in range(k):
                arr[i] += cookies[index]
                calcMin(index + 1, arr)
                arr[i] -= cookies[index]

        calcMin(0, arr)
        return self.minimumUnfairness