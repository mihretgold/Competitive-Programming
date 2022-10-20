#define ll long long;
class Solution {
public:
    int chalkReplacer(vector<int>& chalk, int k) {
        int n = chalk.size();
        long sum = 0;
        for (auto x : chalk) sum += x;
        k = k % sum;
        int i = 0;
        while (k >= chalk[i]) {
            k -= chalk[i];
            i = (i + 1) % n;
        }
        
        return i;
    }
};