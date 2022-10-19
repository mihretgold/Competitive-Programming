class Solution {
public:
    /*
    s,e  k=3 count =0 sum=0
    
    22225558   count=3
    ^ ^ 
    
    while e<n
    for(o-k){sum}
    sum/3 >= t -> counts++
    sum-=arr[s];
    s++;
    e++;
    sum+=arr[e];
    
    
    */
    int numOfSubarrays(vector<int>& arr, int k, int threshold) {
      
        int n= arr.size();
        int s=0, e=0, counts=0, sum=0;
        
        while(e<n){
            while(e-s+1<=k){
                sum+=arr[e];
                e++;
            }
          if(sum/k >= threshold){
              counts++;
          }  
            sum-=arr[s];
            s++;                    
            
        }
       return counts; 
    }
};