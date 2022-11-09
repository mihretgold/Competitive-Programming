class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
      int n=points.size();
      vector<vector<int>>m;
        
        for(int i=0; i<n; i++){
               m.push_back({points[i][0]*points[i][0] + points[i][1]*points[i][1],points[i][0],points[i][1]});//vector holding a vector of the distance,x,y
             
        }
        sort(m.begin(), m.end());
        vector<vector<int>>ans;
        for(int i=0; i<k; i++){
           ans.push_back({m[i][1],m[i][2]});
        }
        return ans;
    }
};