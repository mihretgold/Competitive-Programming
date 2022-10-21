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
    
   // Run time 18
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
    Algorithm
    1) declare a vector to push back non duplicate elements to
    2) and 2 iterators one to find the duplicate and another to find index in vector v
    3) add non duplicate elements to the vector
    4) if duplicate element is found start count from 1 and initialize the 2nd iterator to the begining of the vector
    5) until the 2nd iterator == 1st iterator(we find the duplicate element) we increament count and the 2nd iterator
    6) if the duplicate is at the first element we erase the fisrst element if not we wrase the elements until the duplicate
    7) add the new element to the vector
    8) increment count and decreament erased elements
    9) return count
    
    */
   /* int lengthOfLongestSubstring(string s) {
       int n= s.length();
       int c=0, m=0;
        vector<char>v;
        vector<char>::iterator it,it1;
        for(int i=0; i<n; i++){//iterate through the string
          it=find(v.begin(), v.end(), s[i]);//the iterator will find s[i] on the vector v
            if(it!=v.end()){//if duplicate is found
               int count =1;
                it1=v.begin();
                while(it1!=it){//while it1 is not a duplicate we increase the count
                    it1++;
                    count++;
                }
                if(it==v.begin()) v.erase(it);//if the duplicate element is on the the first element we erase it
                else v.erase(v.begin(), ++it);//until we find the duplicate element we erase all the elements
               v.push_back(s[i]);// add new element to the vector
                c++;//increase count as we add an element to the vector
                c-=count;// we decrease the elements that were erased
            } 
            else{//no duplicate
                v.push_back(s[i]);// add non duplicate elements to the vector
                c++;//increase count as we add an element to the vector
            }
            m= max(m,c);//calculate the max from all
        }
        return m;
    }*/
    
};
