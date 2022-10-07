class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        int  l=0,counts=0;
        int n = people.size(), r= n-1;
        sort(people.begin(), people.end());
        while(l<=r){
           if(people[l] + people[r]<= limit){
               l++;
               r--;
           }
            else{
                r--;
            }
            counts++;
        }
        return counts;
    }
};