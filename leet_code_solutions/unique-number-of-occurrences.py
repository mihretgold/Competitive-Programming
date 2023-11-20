class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurences = set()
        store = defaultdict(int)

        arr.sort()

        for num in arr:
            store[num] += 1

        for num in store:
            if store[num] in occurences:
                return False
            occurences.add(store[num])

        return True
            
        