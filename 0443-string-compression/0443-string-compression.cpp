class Solution {
public:
    /*
                      l
    ["a","a","b","b","c","c","c"]
                              r
    
    ["a","2","b","2","c","3"]
    
    
    //are the arrays sorted
    */
    /*
    Algorithm
    1) initialize l,r,k ptrs
    2) while l<n
    3) r=l
    4) while r<n and elements on the right and left indexes are simillar increament r ptr
    5) put the element on the k index ans increament the k ptr
    6) put the elements count in the k ptr and increament k by converting int to_string()
    7) move the left pointer to the new element
    8) return k
    */
    int compress(vector<char>& chars) {
       int n=chars.size(),l=0,k=0,r=0;
       
        while(l<n){
           while(r<n && chars[r]==chars[l]){// counts same elements
               r++;
           }
           
            chars[k++]=chars[l];//puts the element on the l index on k index
            if(r-l>1){
                for(char s: to_string(r-l)){//apends the elements count after the element
                    chars[k++]=s;
                }
            }
            l=r;//move the left pointer to the new element
        }
        
        return k;
    }
};