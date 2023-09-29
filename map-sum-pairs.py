class TrieNode:
    def __init__(self):
        self.kids = [None for _ in range(26)]
        self.count = [0 for _ in range(26)]
        self.isEnd = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        self.dicts = defaultdict(int)

        

    def insert(self, word: str, val, found) -> None:
        current = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            current.count[index] += val
            if current.kids[index] == None:
                current.kids[index] = TrieNode()

            current = current.kids[index]

        current.isEnd = True
        if word in self.dicts and found == 0:
            self.insert(word, - self.dicts[word], 1)
        
        self.dicts[word] = val

        

    def search(self, word: str) -> bool:
        current = self.root
        value = 0
        # print(current.count[index])
        for ch in word:
    
            index = ord(ch) - ord('a')
            # print(current.kids, current.count)
            if current.kids[index] == None:
                return 0

            value = current.count[index]
            current = current.kids[index]

        return value

class MapSum:

    def __init__(self):
        self.trie = Trie()
        

    def insert(self, key: str, val: int) -> None:
        self.trie.insert(key, val, 0)

    def sum(self, prefix: str) -> int:
        return self.trie.search(prefix)
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)