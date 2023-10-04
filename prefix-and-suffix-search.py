class TrieNode:

    def __init__(self):
        self.childern = {}
        self.find = -1

class Trie:
    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word, idx):
        current = self.root

        for letter in word:
            if letter not in current.childern:
                current.childern[letter] = TrieNode()

            current = current.childern[letter]         
            current.find = idx

        

    def searchString(self, word):
        current = self.root
        for letter in word:
            node = current.childern.get(letter)
            if node == None:
                return -1

            current = node

        
        return current.find
       

class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for idx, word in enumerate(words):
            length = len(word)
            for i in range(length):
                string = word[i:] + "{" + word
                self.trie.insert(string, idx)

        
        

    def f(self, pref: str, suff: str) -> int:
        return self.trie.searchString(suff + "{" + pref)
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)