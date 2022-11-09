class Solution {
public:
    vector<bool> checkArithmeticSubarrays(vector<int>& nums, vector<int>& l, vector<int>& r) {
    vector<bool>ans;
        for(int i=0,j; i<l.size(); i++){
            vector<int>temp(begin(nums)+l[i],begin(nums)+r[i]+1);
            sort(temp.begin(), temp.end());
            for(j=2; j<temp.size(); j++)
                if(temp[j]-temp[j-1]!=temp[1]-temp[0])
                    break;
            ans.push_back(j==temp.size());
        }
        return ans;
    }
};