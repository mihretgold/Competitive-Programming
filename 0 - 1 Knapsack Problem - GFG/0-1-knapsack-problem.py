#User function Template for python3
from collections import defaultdict

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        
        mem = defaultdict(int)
        def calc(index, sums):
            if index >= n:
                return 0
            
            if (index, sums) in mem:
                return mem[(index, sums)]
            
        
            left = calc(index + 1, sums)
            right = 0
            
            if sums + wt[index] <= W:
                right = calc(index + 1, sums + wt[index]) + val[index]
            else:
                right = calc(index + 1, sums)
            
            mem[(index, sums)] += max(left, right)
            
            return mem[(index, sums)]
            
        return calc(0, 0)
                    
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends