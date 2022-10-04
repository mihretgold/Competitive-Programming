class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
      vector<int> counts(temperatures.size(),0);
        stack<int> s;
        int n=temperatures.size();
        for(int i=0; i<n; i++){
            int v=temperatures[i];
            while(!s.empty() && temperatures[s.top()] < v){
                int t=s.top();
                counts[t]= i - t;
                 s.pop();
            }
            s.push(i);
        }
        return counts;
    }
};