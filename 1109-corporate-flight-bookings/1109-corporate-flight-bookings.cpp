class Solution {
public:
    /*
    ans[n,0]
    
    for(b[i][0] -[1])
       ans[]+= b[i][2]
       retun ans
     [1,2,10] 1-2 -> 10 seats
     [2,3,20] 2-3 -> 20 seats
     [2,5,25] 2-5 -> 25 seats 
      f1: 10
      f2: 55
      f3: 45
      f4: 25
      f5: 25
      //make store sum fore inital points only and subtract for final pts
      f1=10  f2+1=f3=-10  
      f2=20  f4=-20
      f2=25  f6=-25 but not needed for >n
      then we add previos and new to find sum of all
      1-2: 10 0 -10 0 0
      2-3: 10 20 -10 -20 0
      2-5: 10 45 -10 -20 0
      final addition with prefix sum
      10 + 45  + -10  + -20 + 0
         = 10 55 45 25 25
    */
    vector<int> corpFlightBookings(vector<vector<int>>& bookings, int n) {
       vector<int>ans(n,0);       
               
        for( auto x: bookings){
           int i= x[0]-1;//first
            int j=x[1];// last
            ans[i]+=x[2];//add seat to initial point
            if(j<n)ans[j]-=x[2];//subract seat to last pt            
        }
        for(int i=1; i<n; i++){//find prefix sum
            ans[i]+=ans[i-1];
        }
        
        return ans;
    }
};