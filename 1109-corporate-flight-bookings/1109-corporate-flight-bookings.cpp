class Solution {
public:
    /*
    ans[n,0]
    
    for(b[i][0] -[1])
       ans[]+= b[i][2]
       retun ans
    */
    vector<int> corpFlightBookings(vector<vector<int>>& bookings, int n) {
       vector<int>ans(n,0); 
        int l=bookings.size();
       
        
        for( auto x: bookings){
           int i= x[0]-1;
            int j=x[1];
            ans[i]+=x[2];
            if(j<n)ans[j]-=x[2];
            
        }
        for(int i=1; i<n; i++){
            ans[i]+=ans[i-1];
        }
        
        return ans;
    }
};