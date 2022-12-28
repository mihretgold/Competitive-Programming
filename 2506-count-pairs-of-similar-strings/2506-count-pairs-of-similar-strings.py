class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0
        length = len(words)
        right = 0
        left = 1
        while(right < length-1):
            set_w1 = list(set(words[right]))
            set_w1.sort()
            set_w2 = list(set(words[left]))
            set_w2.sort()
            if str(set_w1) in str(set_w2):
                count += 1
            if left + 1 == length:
                right += 1
                left = right
            left +=1
            
                
        return count