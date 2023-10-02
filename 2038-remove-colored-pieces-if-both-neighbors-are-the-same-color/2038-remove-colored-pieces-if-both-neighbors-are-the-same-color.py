class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice = 0
        bob = 0
        start = 0
        length = len(colors)
        a_count = 0
        b_count = 0
        
        for end in range(length):
            if colors[end] == "A":
                a_count += 1
            elif colors[end] == "B":
                b_count += 1
                
            if end - start == 2:
                if a_count == 3:
                    alice += 1
                elif b_count == 3:
                    bob += 1
                    
            if end - start >= 2:
                if colors[start] == "A":
                    a_count -= 1
                else:
                    b_count -= 1
                    
                start += 1
                
        return alice > bob
                