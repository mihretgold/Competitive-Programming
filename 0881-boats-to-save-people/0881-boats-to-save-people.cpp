class Solution {
public:
    /*
    Algorithm
    1)declare 2 ptrs one starting from 0 & the other from n-1
    2) sort
    3) while l<=r
    4) add elements on the l & r indexes if <= limit move both ptrs
    5) if not move only r ptr
    4) and increament count each time
    
    
    */
   int numRescueBoats(vector<int>& people, int limit) {
        int  l=0,counts=0;
        int n = people.size(), r= n-1;
        sort(people.begin(), people.end());
        while(l<=r){
           if(people[l] + people[r]<= limit){//if the sum <= limit we move both pointers
               l++;
               r--;
           }
            else{//if > move only r pointer
                r--;
            }
            counts++;
        }
        return counts;
    }
};