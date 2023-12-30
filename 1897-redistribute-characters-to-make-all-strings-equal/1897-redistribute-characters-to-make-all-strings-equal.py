class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        store = defaultdict(int)
        length = len(words)
        
        for row in range(length):
            size = len(words[row])
            for col in range(size):
                store[words[row][col]] += 1
        # print(store)      
        for key, value in store.items():
            # print(value % length)
            if value % length != 0:
                return False
            
        return True