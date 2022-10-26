class Solution {
public:
    /*
    Algorithm
    1) initialize an idx to hold a number starting from the back that is less han the number b/f it
    2) then break when u find 1 num
    3) if no idx is found the nums are in descending we simply sort it
    4) if found we find the element b/f the found index and put it in a variable
    5) then we swap the element with the next largest number 
    6) we sort the nums starting from idx   
    
    
    */
    void nextPermutation(vector<int>& nums) {
        int n=nums.size()-1;
        int ipt=0;
        for(int i=n; i>0; i--){//starting from the end
            if(nums[i]>nums[i-1]){//if the number is less than the number before it 
               ipt=i;// we put the index on ipt variable
                break;// and if we find 1 num we break
            }
        }
        if(ipt==0){//if the nums are in descending we simply sort it
            sort(nums.begin(),nums.end());
        }
        else{// if not
            int toswap =nums[ipt -1];//we find the element b/f the found index and put it in a variable
            int min=INT_MAX;
            for(int j=ipt; j<=n; j++){//from the index found to the end of the array
                if(nums[j]-toswap>0 && nums[j]-toswap<min){//we find the next grater num by making sure its d/f with to swap is > 0 making it grater but also making sure the d/f is 
                    // we swap the element with the next largest number 
                swap(nums[j],nums[ipt-1]); //we can't use toswap instead of nums[ipt-1] because that would swap it with the variable insead if swaping the array elements 
                }
            }
            sort(nums.begin()+ipt,nums.end());//then sort it starting from the found pt
        }
    }
};