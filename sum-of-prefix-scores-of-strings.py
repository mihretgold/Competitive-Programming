class TrieNode:
    def __init__(self):
        self.kids = [None for _ in range(26)]
        self.count = 0
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
            current.count += 1

        current.isEnd = True

        

    def search(self, word: str) -> int:
        current = self.root
        answer = 0
        for ch in word:
            index = ord(ch) - ord('a')
            answer += current.kids[index].count

            current = current.kids[index]

        return answer

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        length = len(words)
        answer = []

        for word in words:
            trie.insert(word)

        for word in words:
            answer.append(trie.search(word))

        return answer