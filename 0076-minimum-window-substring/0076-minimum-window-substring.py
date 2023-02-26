class Solution:
    '''
    A,DOBECODEBA,NC   ABC  
    ch [A:1, B:1, C:1] 1
    mp [A:1, B:2, C:1 ] 0
    '''
    def minWindow(self, s: str, t: str) -> str:
        t_dict = defaultdict(int)
        s_dict = defaultdict(int)
        length_t = len(t)
        length = len(s)
        start = 0
        count = 0
        ranges =[-1,-1]
        mini = length + 1
        
        for index in range(length_t):
            t_dict[t[index]] += 1
            
        window = len(t_dict)
        
        for end in range(length):
            if s[end] in t_dict:
                s_dict[s[end]] += 1
                if s_dict[s[end]] == t_dict[s[end]]:
                    count += 1
                  
            while count == window:
                if end - start + 1 < mini:
                    mini = min(end - start + 1, mini)
                    ranges[0], ranges[1] = start, end
                if start < length and s[start] in s_dict:
                    s_dict[s[start]] -= 1
                    if s[start] == 0:
                        s_dict.pop(s[start])
                    if s_dict[s[start]] < t_dict[s[start]]:
                            count -= 1                
                start += 1
        
        answer = s[ranges[0]:ranges[1] + 1]
        
        return answer