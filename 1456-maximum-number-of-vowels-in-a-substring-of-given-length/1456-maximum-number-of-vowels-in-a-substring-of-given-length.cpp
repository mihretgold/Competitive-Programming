class Solution {
public:
    /*
     s = "abciiidef", k = 3  count=0
     //ask if all capital or lowercase letters
             
    */
    int maxVowels(string s, int k) {
      int n=s.size();
        int l=0,r=0,count=0,m=0;
        while(r<n){
            // add k number of elements to the window
            while(r-l+1<=k){
                if(s[r]=='a'|| s[r]=='e'|| s[r]=='i'|| s[r]=='o'|| s[r]=='u'){//if vowel increament count
                    count++;
                }
                r++;
            }
            m=max(m,count);
             if(s[l]=='a'|| s[l]=='e'|| s[l]=='i'|| s[l]=='o'|| s[l]=='u'){//if vowel decreament count
                    count--;
                }
            l++;
            
        }
        return m;
    }
};