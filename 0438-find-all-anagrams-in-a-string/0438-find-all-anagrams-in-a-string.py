class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window = len(p)
        p_dict = defaultdict(int)
        
        length = len(s)
        start = 0
        for i in range(window):
            p_dict[p[i]] += 1
            
        answer = [] 
        end = 0
        s_dict = defaultdict(int)
        while end < length:
            while end - start < window and end < length:
                s_dict[s[end]] += 1
                end += 1
            
            if s_dict == p_dict:
                answer.append(start)
            if s_dict[s[start]] == 1:
                s_dict.pop(s[start])
            elif s_dict[s[start]] > 0:
                s_dict[s[start]] -= 1
            start += 1
            
        return answer
                
                