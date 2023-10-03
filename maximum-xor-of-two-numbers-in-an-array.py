class TrieNode:
    def __init__(self):
        self.kids = [None for _ in range(2)]
        self.isEnd = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for ch in word:
            index = int(ch)
            if current.kids[index] == None:
                current.kids[index] = TrieNode()

            current = current.kids[index]

        current.isEnd = True

    def search(self, word: str):

        answer = 0
        current = self.root
        for i, ch in enumerate(word):
            index = int(ch)
            # print(index ^ 1)
            if current.kids[index ^ 1] == None:
                current = current.kids[index]
            else:
                answer += 1 << (len(word) - i - 1)
                current = current.kids[index ^ 1]

        return answer






class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = {}

        size = len(bin(max(nums))) - 2
        trie = Trie()
        length = len(nums)
       
        

        answer = 0
        for num in nums:
            current = root
            for i in range(size, -1, -1):
                index = (num >> i) & 1
                if index not in current:
                    current[index] = {}
    
                current = current[index]
        maxx = 0
        for num in nums:
            current = root
            answer = 0
            for i in range(size, -1, -1):
                index = (num >> i) & 1
                if (index ^ 1) not in current:
                    current = current[index]
                else:
                    current = current[index ^ 1]
                    answer += 1 << i

            maxx = max(maxx, answer)

        return maxx