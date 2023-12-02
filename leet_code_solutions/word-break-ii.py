class TrieNode:

    def __init__(self):
        self.childern = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root

        for letter in word:
            node = current.childern.get(letter)
            if node == None:
                node = TrieNode()
                current.childern[letter] = node

            current = node
        current.end = True
        

    def searchString(self, word):
        current = self.root
        for letter in word:
            node = current.childern.get(letter)
            if node == None:
                return False

            current = node

        if current.end == True:
            return True
        else:
            return False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        root = trie.root

        arr = []
        
        def bt(index, path):
            current = trie.root
            for idx in range(index, len(s)):
                if s[idx] not in current.childern:
                    return 
                current = current.childern[s[idx]]
                
                path.append(s[idx])

                if current.end:
                    if idx == len(s) - 1:
                        arr.append("".join(path))
                        return 
                    
                    bt(idx + 1, path + [" "])

               

        bt(0, [])

        return arr
            
       









        