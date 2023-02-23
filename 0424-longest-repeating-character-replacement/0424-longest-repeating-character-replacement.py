class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxi = 0
        maxfreq = 0
        start = 0
        length = len(s)
        letter = defaultdict(int)
        for end in range(length):
            letter[s[end]] += 1
            maxfreq = max(maxfreq, letter[s[end]])
            while (end - start + 1) - maxfreq > k:
                letter[s[start]] -= 1
                start += 1
                
            maxi = max(maxi, end-start+1)
            
        return maxi