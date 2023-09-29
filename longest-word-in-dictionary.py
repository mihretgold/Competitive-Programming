class TrieNode:
    def __init__(self):
        self.kids = [None for _ in range(26)]
        self.isEnd = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        current = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if current.kids[index] == None:
                current.kids[index] = TrieNode()

            current = current.kids[index]

        current.isEnd = True
        
        

        

    def search(self, word: str) -> bool:
        current = self.root
        
        for ch in word:
            index = ord(ch) - ord('a')
            if current.kids[index].isEnd == False:
                print(ch, current.isEnd)
                return 0

            current = current.kids[index]

        return len(word)
class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        maxi = (0, "")
        for word in words:
            trie.insert(word)

        for word in words:
            value = trie.search(word)
            
            if value > maxi[0]:
                maxi = (value, word)
            elif value == maxi[0]:
                wordNew = maxi[1]
                if word < maxi[1]:
                    maxi = (value, word)
        

        return maxi[1]