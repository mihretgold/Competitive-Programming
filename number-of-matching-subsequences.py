class TrieNode:
    def __init__(self):
        self.kids = [None for _ in range(26)]
        self.isEnd = False
        self.wordCount = 0


class Trie:

    def __init__(self):
        self.root = TrieNode()
        self.count = 0
        

    def insert(self, word: str) -> None:
        current = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if current.kids[index] == None:
                current.kids[index] = TrieNode()

            current = current.kids[index]

        current.isEnd = True
        current.wordCount += 1

    def indexFinder(self, word, start, char):
        length = len(word)
        for idx in range(start, length):
            if word[idx] == char:
                return idx

        return -1

    def search(self, word, node, idx):
       for i in range(26):
           char = chr(i + ord('a'))

           if node.kids[i] != None:
               child = node.kids[i]
               index = self.indexFinder(word, idx, char)

               if index != -1:
                   if child.isEnd:
                       self.count += child.wordCount
                   self.search(word, child, index + 1)


                    







class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        trie = Trie()
        
        for word in words:
           trie.insert(word)

        trie.search(s, trie.root, 0)

        return trie.count