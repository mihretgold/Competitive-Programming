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
    def insertWord(self, word: str) -> str:
        answer = ""
        current = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if current.kids[index] == None or current.isEnd:
                break
            else:
                answer += ch

            current = current.kids[index]

        current.isEnd = True
        return answer

        

   
        

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        length = len(strs)

        val = ""
        if length > 0:
            trie.insert(strs[0])
            val = trie.insertWord(strs[0])

        for index in range(1, length):
            val = trie.insertWord(strs[index])

        return val

        