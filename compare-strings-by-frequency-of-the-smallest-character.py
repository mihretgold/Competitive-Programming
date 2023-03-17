class Solution:
    def frequencySmallest(self, arr):
        answer = []
        for word in arr:
            dicts = defaultdict(int)
            for letter in word:
                dicts[letter] += 1

            words = list(dicts.keys())
            minLetter = min(word)
            answer.append(dicts[minLetter])

        return answer
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        answer = []
        queriesNum = self.frequencySmallest(queries)
        wordsNum = self.frequencySmallest(words)
        wordsNum.sort()
        for num in queriesNum:
            low = 0
            high = len(words)-1
            while low <= high:
                mid = low + (high - low)//2
                if num < wordsNum[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            answer.append(len(words) - low)

        return answer