class Trie:

    def __init__(self):
        self.prefixTree = []


    def insert(self, word: str) -> None:
        self.prefixTree.append(word)

    def search(self, word: str) -> bool:
        check = False
        for preWord in self.prefixTree:
            if preWord == word:
                check = True

        return check

    def startsWith(self, prefix: str) -> bool:
        check = False
        for preWord in self.prefixTree:
            if preWord.startswith(prefix):
                check = True

        return check


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)