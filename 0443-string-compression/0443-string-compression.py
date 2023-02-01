class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        length = len(chars)
        index = 0
        count = 0
        
        for right in range(length):
            if chars[left] != chars[right]:
                chars[index] = chars[left]
                index += 1
                count += 1
                if right - left > 1:
                    k = str(right - left)
                    for num in k:
                        chars[index] = num
                        index += 1
                        count += 1
                if right == length-1:
                    chars[index] = chars[right]
                    index += 1
                    count += 1
                left = right 
            elif right == length-1:
                chars[index] = chars[right]
                index += 1
                count += 1
                if right - left > 0:
                    k = str(right - left + 1)
                    for num in k:
                        chars[index] = num
                        index += 1
                        count += 1
                left = right 
                
       
            
        return count