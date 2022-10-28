class Solution {
public:
/*   0 1 2 3 4 5
    [1,7,3,6,5,6]   sum=28  bsum=6  
     1 8 11172228      =22 sum -nums[i]     =11 bsum+= nums[i]
     2827201711 6      =17      =17
    [2,1,-1]      
     2 3 2
     2 0 -1
     [-1,-1,0,0,-1,-1]
      -1  -2 -2 -2 -3 -4
      -4 -3 -2 -2 -2  -1
    */
int pivotIndex(vector<int>& nums) {
     int sum=0;
        for(int i: nums){//add all elements to sum
            sum += i;
        }
        int p=0;//front sum of the array
        for(int i=0; i<nums.size(); i++){
            if(sum-p-nums[i] == p){//if pront sum== sum -p - nums[i] then we return i
                return i;
            }
            p+=nums[i];//add the elements to front sum until it's equal
        }
      return -1; //if no left sum return -1 
    }
};
    
