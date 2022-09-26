class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string>answer;
        for(int i=1;i<=n;i++)
        {
            string ans;
            if(i%3==0)
                ans+="Fizz";
            if(i%5==0)
                ans+="Buzz";
            if(ans.length()==0)
                ans=to_string(i);
            answer.push_back(ans);
                
        }
        return answer;
    }
};