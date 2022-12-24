class Solution:
    
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word_list1=list(word1)
        word_list2=list(word2)
        length1=len(word_list1)
        length2=len(word_list2)
        
        index1=0
        index2=0
        appended=""
        while(index1 < length1 and index2 < length2):
            appended += word_list1[index1]
            index1 += 1
            appended += word_list2[index2]
            index2 += 1
            
        while(index1 < length1):
            appended += word_list1[index1]
            index1 += 1
            
        while(index2 < length2):
            appended += word_list2[index2]
            index2 += 1
            
        return appended