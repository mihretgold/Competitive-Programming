class Solution {
public:
    /*
    "abcabcbb"
        ^  ^
      i,j
      hash map >1
      find index +1
     1) Brute force apprach 
    "abcabcbb"
      ^   ^
   i=0 j=0 y=0  ans=1
   i=1 j=0 y=0  ans=2 
   i=2 j=0 y=0  ans=3 
   i=3 j=0 y=1  ans=3 
   i=4 j=1 y=2  ans=3 ...
   
       i,j,ans, y=0

    
    */
    /*
    Algorithm
    1) nested loop with first loop iterating through the sring
    2) And the second loop searching for duplicate elements
    3) start the second loop from the found element + 1 or zero until dulicate element is found
    4) inside loops if duplicate is found from 0(found e+1) to < element j is at the iteration of the 1st loop
    5)after the second loop calculate max sub array
    
    */
   /* int lengthOfLongestSubstring(string s) {
       int i,ans=0,y=0;
        for(int j=0;j<s.size();j++)// iterates through string
        {
            
            for(i=y;i<j;i++) // if i<j iterates to check any simillar elements
            {
            // if similar elements are found increaments the starting index of i to start from the found element+1
                if(s[i]==s[j])
                {
                    y=i+1;  
                }
            }
              ans=max(ans,j-y+1); //puts max subarray to ans variable          
        }
        return ans;
    }*/
    
   // Run time 39
    /*
    Algorithm
    1) initialize unordered map to hold each chat and its counts
    2) as long as the right ptr > s.size()
    3) add count ant char to map and increamnt r index
    4) if a duplicate is found meaning the count in the map > 0
    5) we will first calculate the max length with r-l since index r is at the duplicate number
    6) while the element pointed by the right index is not equal to the element pointed by the left index(the duplicate)we increament the left pointer and decreament the count from the map
    7) then when we find the duplicate element and decrease the count on the map 
    8)if there is no duplicate and/or if the right ptr == n-1 we put the max length as r-l+1 since the r element is not a duplicate
    
    
    */
 /*  int lengthOfLongestSubstring(string s) {
        int i=0, j=0, maxlen=0, len=0;
        unordered_map<char,int> mymap;
        while(j<s.length()){ 
            if(mymap[s[j]]>0){ //if the count of the element is >0 or when we find a duplicate
                len = j-i;
                maxlen = max(maxlen, len);
                while(s[j]!=s[i]){ //when index i is not the index holding the duplicate
                    mymap[s[i]]--;//we decreament the count of the element
                    i++;//and increament the index
                }mymap[s[i]]--;
                 i++;
            }else if(j==s.length()-1){//at the end of the string
                len = j-i+1;
                maxlen = max(maxlen, len);
            }
            mymap[s[j]]++;//if the element is not a duplicate we store the element and count on the map
            j++;
        }
        return maxlen;
    }*/
    /*
    012345678
    bcaaghji
        ^  ^
   abc
   
    */
   int lengthOfLongestSubstring(string s) {
    unordered_map<char,int>m;
       int n=s.size(),l=0, r=0,maxi=0;
       while(r<n){
           if(m[s[r]] >0){// duplicate elements
            maxi=max(maxi, r-l);
               while(s[l]!=s[r]){// until we find duplicate element
                m[s[l++]]--;   
               }
               m[s[l++]]--; // when the duplicate element is found
           }else if(r==n-1){// at end string
               maxi=max(maxi,r-l+1);
           }
            m[s[r++]]++;//non duplicate elements
           
       }
       return maxi;
 } 
    
    
    
 /*
 Run time 45ms
 int lengthOfLongestSubstring(string s) {
     unordered_map<char, int> m; //character map to index
     int maxi = 0, l = 0, r = 0;
     
     while (r < size(s)) {
         if (m.find(s[r]) == m.end() || m[s[r]] < l) //element not duplicate
             maxi = max(maxi, r-l+1);
         else  l = m[s[r]] + 1;//element is duplicate
         m[s[r++]] = r; //update element in map, and increment r;
     }
     return maxi;
 }*/
  /*  
  Run time 23ms
  int lengthOfLongestSubstring(string s) {
        vector<int> dict(256, -1);
        int maxLen = 0, start = -1;
        for (int i = 0; i != s.length(); i++) {
            if (dict[s[i]] > start)// if duplicate found
                start = dict[s[i]];
            dict[s[i]] = i;
            maxLen = max(maxLen, i - start);
        }
        return maxLen;
    }  */
    
    
    
};
