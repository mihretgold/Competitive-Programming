class Solution:
    '''
    must find a smallest substring where we can replace the missing letters
    find max subarray with size >= num of missing
    '''
    def balancedString(self, s: str) -> int:
        check = {"Q":0, "W":0, "E":0, "R":0 }
        length = len(s)
        count = 0
        sums = 0
        surplus = defaultdict(int)

        for letter in s:
            check[letter] += 1
            if check[letter] == length // 4:
                count += 1
            if count == 4:
                return 0

        for value in check:
            if (check[value] - length//4) > 0:
                surplus[value] = check[value] - length//4
            sums += abs(check[value] - length//4)
        
        sums //= 2
        start = 0
        mini = length + 1
        window = 0
        word = defaultdict(int)
        
        for end in range(length):
            if s[end] in surplus:
                word[s[end]] += 1
                if word[s[end]] <= surplus[s[end]]:
                # print( word[s[end]], surplus[s[end]])                
                    window += 1

            while window >= sums:
                mini = min(mini, end - start + 1)
                print(start, end, mini)
                if s[start] in word:
                    if word[s[start]] <= surplus[s[start]]:
                        window -= 1
                    word[s[start]] -= 1
                    if  word[s[start]] == 0:
                        word.pop(s[start])
                    
                start += 1
                


        

        return mini