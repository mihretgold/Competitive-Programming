class Solution:
#     Algorithm
# s1. create 2 hash maps and store the count of each 
# s2. compare the 2 hash maps and display the unique one

    def findTheDifference(self, s: str, t: str) -> str:
        #put the letters and counts in string to dictionary 
        map_s={}
        for letter in s:
            if letter in map_s:
                map_s[letter] += 1
            else: 
                map_s[letter] = 1            
            
        map_t={}
        for letter in t:
            if letter in map_t:
                map_t[letter] += 1
            else: 
                map_t[letter] =1          
          
        for compare in map_t:
            if compare not in map_s or map_t[compare] != map_s[compare]:
                
                return compare
           
            