class Solution {
public:
    int maxArea(vector<int>& height) {
      int w=0, l=0, r=height.size()-1;
        while(l<r){
            int a;
            // we  first have to check which element is < b/c the lesser element decides the height
            if(height[l] < height[r]){//if the element pointed by the l is < we pick it as height and increament the l ptr
            a= height[l] * (r-l);
                l++;
            }
            else{//if the element pointed by the r is < we pick it as height and decreament the r ptr
                a=height[r] * (r-l);
                r--;
            }
            w=max(w,a);//store max area
        }
        return w;
    }
};