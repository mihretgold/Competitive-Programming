#define ll long long;
class Solution {
public:
    int chalkReplacer(vector<int>& chalk, int k) {
        int n = chalk.size();
        long sum = 0;
        for (auto x : chalk) sum += x;//sum of all elements in the array
        k = k % sum;//to simplify reapeated subtraction
        int i = 0;
        while (k >= chalk[i]) {//while k > the elements in the array we increament i
            k -= chalk[i];
            i = (i + 1) % n;//if i becomes greater than n
        }
        
        return i;
    }
};