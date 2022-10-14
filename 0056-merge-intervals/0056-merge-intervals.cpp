class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
       int n=intervals.size(),j=0;
        vector<vector<int>> ans;
        sort(intervals.begin(), intervals.end());
        ans.push_back(intervals[0]);
        
        for(int i=1; i<n; i++){
            if(ans[j][1]>=intervals[i][0]){
                ans[j][1]=max(ans[j][1],intervals[i][1]);
            }
            else{
                 j++;
                 ans.push_back(intervals[i]);
            }
        }
        return ans;
    }
};