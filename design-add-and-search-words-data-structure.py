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
            if ch == ".":
                queue = deque()
                for i in range(26):
                    if current.kids[i] != None:
                        queue.append(current.kids[i])
            else:
                found = 0
                while queue:
                    index = ord(ch) - ord('a')
                    length = len(queue)
                   
                    node = queue.popleft()

                    for child in node.kids:
                        if child == ch:
                            found = child
                            break
                    if found != 0 and found.isEnd:
                        return True
        return False



        if current.isEnd == True:
            return True
        else:
            return False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if current.kids[index] == None:
                current.kids[index] = TrieNode()

            current = current.kids[index]

        current.isEnd = True

    def search(self, word: str) -> bool:
        current = self.root
        isFound = True
        queue = deque()
        queue.append(current)
        for ch in word:
            index = ord(ch) - ord('a')
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                if ch == ".":
                    for i in range(26):
                        if node.kids[i] :
                            queue.append(node.kids[i])
                else:                  
                        

                    if node.kids[index] != None:
                        queue.append(node.kids[index])
            
            if not queue:
                return False
                
        for value in queue:
            if value.isEnd :
                return True
           

        return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)