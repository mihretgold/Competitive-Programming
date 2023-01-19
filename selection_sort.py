class Solution: 
    def select(self, arr, i):
        # code here 
        for a in range(i, n):
            mini = a
            for j in range(a+1, n):
                if arr[j] < mini:
                    mini = j
        return mini
        
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            mini = i
            for j in range(i+1, n):
                if arr[j] < arr[mini]:
                    mini = j
            arr[i], arr[mini] = arr[mini], arr[i]
