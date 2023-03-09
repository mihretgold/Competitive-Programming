class Solution {
public:
 int shortestSubarray(vector<int>& A, int K) {
        int N = A.size(); 
        long long res = N + 1;
        vector<long long> S (N + 1, 0);
        for(int i = 0; i < N; i++) S[i + 1] = S[i] + A[i];
        deque<int> d;
        for(int i = 0; i < N + 1; i++){
            while(d.size() > 0 && S[i] - S[d.front()] >= K){
                res = min(res, (long long)(i - d.front())); 
                d.pop_front();
            }
           
            while(d.size() > 0 && S[i] <= S[d.back()]){
                d.pop_back();
            }
            d.push_back(i);
        }

        return res == N + 1? -1: res;
    }
};