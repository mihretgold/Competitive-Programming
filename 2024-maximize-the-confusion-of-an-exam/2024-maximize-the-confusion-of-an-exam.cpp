class Solution {
public:
    int maxConsecutiveAnswers(string s, int k) {
        int n=s.size(),j=0;
    int maxi=0,fc=0;
   for(int i=0; i<n; i++){
      if(s[i] == 'F') fc++;
       while(fc > k){
            if(s[j] == 'F') fc--;
           j++;
       }
       maxi=max(maxi,i-j+1);
   }
     fc=0;j=0; 
   for(int i=0; i<n; i++){
      if(s[i] == 'T') fc++;
       while(fc > k){
            if(s[j] == 'T') fc--;
           j++;
       }
       maxi=max(maxi,i-j+1);
   }
    return maxi;
    }
};