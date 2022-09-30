
class Solution {
public:
    string sortSentence(string s) {
     string word;
        vector<string>v(10);
        for(int i=0; i<s.size(); i++){
             // check if number
            if(s[i]>= 48 && s[i]<=57){             
                v[s[i] - 48] = word + " ";
                word = ""; // starts from empty again
                i++; // since next char will be space to skip it
            }
            else
            word+= s[i];
        }
        string ans;
        for(string x:v){
            ans+=x;
        }
        ans.pop_back();
        return ans;
    }
};