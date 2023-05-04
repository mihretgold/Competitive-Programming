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