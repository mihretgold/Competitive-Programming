class Solution {
public:
    static bool cmp(string &a, string &b){
        return (a+b)>=(b+a);
    }
    string largestNumber(vector<int>& nums) {
        vector<string>s(nums.size(),"");
        int x=0;
        for(int i=0; i<nums.size(); i++){
           if(nums[i]==0){
               x++;
           }
        }
        if(x==nums.size()) return "0";
        
        for(int i=0; i<nums.size(); i++){
            s[i]=to_string(nums[i]);
        }
        sort(s.begin(),s.end(),cmp);
        string ans="";
        for(int i=0; i<s.size(); i++){
            ans+=s[i];
        }
        return ans;
    }
};