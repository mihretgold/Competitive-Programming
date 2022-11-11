class Solution {
public:
    /*static bool cmp(string &a, string &b){
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
        
        for(int i=0; i<nums.size(); i++){
            s[i]=to_string(nums[i]);
        }
        sort(s.begin(),s.end(),cmp);
        string ans="";
        for(int i=0; i<s.size(); i++){
            ans+=s[i];
        }
        return ans;*/
    static bool cmp(string &a, string&b){
    return a+b>=b+a;
}
string largestNumber(vector<int>& nums){
   int n=nums.size(),count=0;
    for(int x: nums){
        if(x==0) count++;
    }
    //if all elements are 0
    if(count ==n) return "0";
    vector<string>s(n,"");
    for(int i=0; i<n; i++){
        s[i]+=to_string(nums[i]);
    }
    sort(s.begin(),s.end(),cmp);
    string ans="";
    for(int i=0; i<n; i++){
        ans+=s[i];
    }
    return ans;
}
};