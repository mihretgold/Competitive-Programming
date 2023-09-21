class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1) + len(nums2)
        length1 = len(nums1)
        length2 = len(nums2)
        
        i = 0
        j = 0
        index = 0
        num = [0, 0]
        foundans = [0, 0]
        while i < length1 and j < length2:
            index += 1
            if nums1[i] <= nums2[j]:
                if index == length//2:                                  
                    num[0] = nums1[i]
                    foundans[0] = 1
                elif index == length//2 + 1:
                    num[1] = nums1[i]
                    foundans[1] = 1
                    break
               
                i += 1
            else:
                if index == length//2:                                   
                    num[0] = nums2[j]
                    foundans[0] = 1
                elif index == length//2 + 1:
                    num[1] = nums2[j]
                    foundans[1] = 1
                    break
                
                j += 1

                
            
            
        
        while i < length1:
            index += 1
            if index == length//2 and not foundans[0]:
                num[0] = nums1[i]
                
            elif index == length//2 + 1 and not foundans[1]:
                num[1] = nums1[i]
                break
            i += 1
                
        while j < length2:
            index += 1
            if index == length//2 and not foundans[0]:
                num[0] = nums2[j]
                
            elif index == length//2 + 1 and not foundans[1]:
                num[1] = nums2[j]
                break
            
            j += 1

        if length & 1:
            return num[1]
        else:
            return (num[0] + num[1]) / 2
        
            
            
        
            
        