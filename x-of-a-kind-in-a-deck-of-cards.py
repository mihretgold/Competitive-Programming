class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)
        check = True
        freq = count[deck[0]]
        

        for num in count:
            freq = math.gcd(freq,count[num])
            if math.gcd(freq,count[num]) == 1:
                check = False
                break

        return check