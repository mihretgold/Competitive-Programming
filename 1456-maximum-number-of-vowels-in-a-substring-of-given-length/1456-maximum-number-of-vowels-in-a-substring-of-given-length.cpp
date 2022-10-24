/*class Solution {
public:
    /*
     s = "abciiidef", k = 3  count=0
     //ask if all capital or lowercase letters
             
    */
  /*  int maxVowels(string s, int k) {
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
};*/
class Solution {
public:
    
    int maxVowels(string s, int k) {
     queue<char> q;
        int cnt=0;
        int maxi=0;
        for(int i=0,j=0;i<s.length();i++)
        {
            if(s[i]=='a' || s[i]=='e' ||s[i]=='i' ||s[i]=='o' ||s[i]=='u' )//check if elements are vowel
            {
                cnt++;
            }
            if(i-j+1==k)//limit window size
            {
                maxi=max(maxi,cnt);
               if(s[j]=='a'|| s[j]=='e'|| s[j]=='i'|| s[j]=='o'|| s[j]=='u')//check if elements are vowel
                {
                    cnt--;
                }
                j++;
            }
        }
        return maxi; 
    }
};
























