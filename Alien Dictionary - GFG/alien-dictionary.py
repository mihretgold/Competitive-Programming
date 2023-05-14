#User function Template for python3
from collections import defaultdict
from collections import deque
  # # code here
    # {"baa","abcd","abca","cab","cad"}
    # b > a 
    # d > a
    # b > d
    # a > c
    # {"caa","aaa","aab"}
    
    # c > a
    # a > b
    
    # ab abcd
    # abc cba dfe
    # Algorithm 
    # 1) make directed graph
    # 2) indegree
    # 3) traverse
    # abc bac def efe

class Solution:
    def findOrder(self,alien_dict, N, K):
    
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for index in range(N-1):
            size = min(len(alien_dict[index]), len(alien_dict[index+1]))
            for letter in range(size):
                if alien_dict[index][letter] != alien_dict[index+1][letter]:
                     graph[alien_dict[index][letter]].append(alien_dict[index+1][letter])
                     indegree[alien_dict[index+1][letter]] += 1
                     if alien_dict[index][letter] not in indegree:
                         indegree[alien_dict[index][letter]] = 0
                     break
        
        queue = deque()
        visted = set()
        
        for letter in indegree:
            if indegree[letter] == 0:
                queue.append(letter)
                visted.add(letter)
                
        answer = []
        
        while queue:
            node = queue.pop()
            answer.append(node)
            
            for child in graph[node]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
                    visted.add(child)
                    
        for ascii in range(ord('a'), ord('a')+K):
            letter = chr(ascii)
            if letter not in visted:
                answer.append(letter)
                
              
        return answer
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends