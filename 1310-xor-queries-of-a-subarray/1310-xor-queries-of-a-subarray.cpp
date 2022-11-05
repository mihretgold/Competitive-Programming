class Solution {
public:   
    vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& queries) {
       int n=arr.size();
        vector<int>pre(n);
        pre[0]=arr[0];
        for(int i=1; i<n; i++){//find prefix XOR
            pre[i]=pre[i-1] ^ arr[i];
        }
        vector<int>ans;
        for(int i=0; i<queries.size(); i++){
            if(queries[i][0]!=0){//if the quries index doesn't start from 0
                //the ans will be XOR of the last index on prefix XOR with the starting index -1
                int temp=pre[queries[i][1]]^ pre[queries[i][0]-1];
                ans.push_back(temp);
            }
            else{//if the quries index starts from 0 we simply push the prefix XOR at the last index
                ans.push_back(pre[queries[i][1]]);
            }
        }
        return ans;
    }
};