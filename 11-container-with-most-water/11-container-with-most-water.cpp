class Solution {
public:
    int maxArea(vector<int>& height) {
      int w=0, l=0, r=height.size()-1;
        while(l<r){
            int a;
            if(height[l] < height[r]){
            a= height[l] * (r-l);
                l++;
            }
            else{
                a=height[r] * (r-l);
                r--;
            }
            if(a > w)
                w=a;
        }
        return w;
    }
};