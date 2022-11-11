class Solution {
public:
    static bool cmp(string &a, string &b){
        return (a+b)>=(b+a);
    }
    string largestNumber(vector<int>& nums) {
        vector<string>s(nums.size(),"");
        int x=0;
        for(int i=0; i<nums.size(); i++){//keep count for zeros
           if(nums[i]==0){
               x++;
           }
        }
        if(x==nums.size()) return "0";//if all elements are 0 we return "0"
        
        for(int i=0; i<nums.size(); i++){//put all the int to string vector
            s[i]=to_string(nums[i]);
        }
        sort(s.begin(),s.end(),cmp);//sort with custom comparator
        string ans="";
        for(int i=0; i<s.size(); i++){//append the answer to a string
            ans+=s[i];
        }
        return ans;
    }
};