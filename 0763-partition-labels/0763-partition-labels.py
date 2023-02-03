class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        map_letter = defaultdict(int)
        length = len(s)
        maxi = 0
        ans = []
        sum = 0
        
        for index in range(length):
            map_letter[s[index]] = index
            
        for index in range(length):
            maxi = max(maxi, map_letter[s[index]])
            if maxi == index:
                idx = index - sum + 1
                sum += idx
                ans.append(idx)
                
                
        return ans