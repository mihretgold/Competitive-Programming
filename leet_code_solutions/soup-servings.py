class Solution:
    def soupServings(self, n: int) -> float:
        m = ceil(n/25)
        @cache
        def calc(a, b):
            if a <= 0 and b > 0:
                return (1, 0)
            elif b <= 0 and a <= 0:
                return (0, 1)
            elif b <= 0 and a > 0:
                return (0, 0)

            first = calc(a - 4, b)
            second = calc(a - 3, b - 1)
            third = calc(a - 2, b - 2)
            fourth = calc(a - 1, b - 3)

            full = first[0] + second[0] + third[0] + fourth[0]
            half = first[1] + second[1] + third[1] + fourth[1]

            return (full/4 , half/4)

        for num in range(1, m + 1):
            val = calc(num, num)
            val = (val[0] + (val[1] * 0.5)) 
            if val > 1 - 1e-5:
                return 1.0

        answer = calc(m, m)
        answer = (answer[0] + (answer[1] * 0.5)) 

       
        return answer   
