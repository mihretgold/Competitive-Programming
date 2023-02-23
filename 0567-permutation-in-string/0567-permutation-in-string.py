class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict_s1 = defaultdict(int)
        window = len(s1)
        length = len(s2)
        start = 0
        
        for letter in s1:
            dict_s1[letter] += 1
            
        dict_s2 = defaultdict(int)
        for end in range(length):
            dict_s2 [s2[end]] += 1
            if end - start + 1 == window:
                if dict_s2 == dict_s1:
                    return True
                dict_s2[s2[start]] -= 1
                if dict_s2[s2[start]] == 0:
                    dict_s2.pop(s2[start])
                start += 1
                
        return False
            