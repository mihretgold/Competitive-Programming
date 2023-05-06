class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        length1 = len(nums1)
        length2 = len(nums2)
        heap = []
        heappush(heap, (nums1[0]+nums2[0], 0, 0))
        answer = []
        visted = set()
        visted.add((0, 0))

        while len(answer) < k and heap:
            sums, index1, index2 = heappop(heap)
            
            answer.append([nums1[index1], nums2[index2]])
            if index2 + 1 < length2 and (index1, index2+1) not in visted:
                heappush(heap, (nums1[index1]+nums2[index2+1], index1, index2+1))
                visted.add((index1, index2+1))
            if index1 + 1 < length1 and (index1+1, index2) not in visted:
                heappush(heap, (nums1[index1+1]+nums2[index2], index1+1, index2))
                visted.add((index1+1, index2))

        return answer