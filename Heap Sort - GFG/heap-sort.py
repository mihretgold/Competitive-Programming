#User function Template for python3

class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        child = i
        left = 2*i + 1
        right = 2*i + 2
        
        if left < n and arr[left] > arr[child]:
            child = left
        
        if right < n and arr[right] > arr[child]:
            child = right
            
        if child != i:
            arr[child], arr[i] = arr[i], arr[child]
            self.heapify(arr, n, child)
        
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        for index in range(n-1//2, -1, -1):
            self.heapify(arr, n, index)
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        self.buildHeap(arr, n)
        for index in range(n-1, -1, -1):
            arr[index], arr[0] = arr[0], arr[index]
            self.heapify(arr, index, 0)
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends