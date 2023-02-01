class Solution:
    def compress(self, chars: List[str]) -> int:
        length = len(chars)
        index = 0
        i = 0
        
        while i < length:
            j = i + 1
            while j < length and chars[i] == chars[j]:
                j += 1
            
            chars[index] = chars[i]
            index += 1
            count = str(j - i)
            if count != '1':
                for k in count:
                    chars[index] = k
                    index += 1
            i = j
            
        return index
        
        # for right in range(length):
        #     if chars[left] != chars[right]:
        #         chars[index] = chars[left]
        #         index += 1
        #         if right - left > 1:
        #             k = str(right - left)
        #             for num in k:
        #                 chars[index] = num
        #                 index += 1
        #         left = right 
            #     if right == length-1:
            #         chars[index] = chars[right]
            #         index += 1
            #     left = right 
            # elif right == length-1:
            #     chars[index] = chars[right]
            #     index += 1
            #     if right - left > 0:
            #         k = str(right - left + 1)
            #         for num in k:
            #             chars[index] = num
            #             index += 1
            #     left = right 
                
       
            
        return index