class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordKey = Counter(words)
        arr = []
        answer = []
        for key in wordKey:
            arr.append((-wordKey[key], key))
        heapify(arr)
        while len(answer) < k:
            answer.append(arr[0][1])
            heappop(arr)


        
        return answer