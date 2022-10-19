class Solution {
public:
    int find_max(vector<int>& nums, int firstLen, int secondLen) {
        int n = nums.size();
        vector<int> dpfirst(n);
        vector<int> dpsecond(n);
        int sum=0;
        for(int i=0; i<n; i++){
            if(i<secondLen){
                sum += nums[i];
                dpfirst[i] = sum;
            }else{
                sum +=nums[i] - nums[i-secondLen];
                dpfirst[i] = max(dpfirst[i-1] , sum);
            }
        }
        sum = 0;
        for(int j=n-1; j>=0; j--){
            if(j+firstLen >= n){
                sum += nums[j];
                dpsecond[j] = sum;
            }else{
                sum += nums[j] - nums[j+firstLen];
                dpsecond[j] = max(dpsecond[j+1] , sum);
            }
        }
        int answer=0;
        for(int k=secondLen-1; k<n-firstLen; k++)
            answer = max(answer, dpfirst[k]+dpsecond[k+1]);
        return answer;
    }
    int maxSumTwoNoOverlap(vector<int>& nums, int firstLen, int secondLen){
        return max(find_max(nums, firstLen, secondLen), find_max(nums, secondLen, firstLen));
    }
};