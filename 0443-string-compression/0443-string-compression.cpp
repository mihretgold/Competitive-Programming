class Solution {
public:
    int compress(vector<char>& chars) {
       int n=chars.size(),l=0,k=0;
       
        while(l<n){
            int r=l;
           while(r<n && chars[r]==chars[l]){
               r++;
           }
           
            chars[k++]=chars[l];
            if(r-l>1){
                for(char s: to_string(r-l)){
                    chars[k++]=s;
                }
            }
            l=r;
        }
        
        return k;
    }
};