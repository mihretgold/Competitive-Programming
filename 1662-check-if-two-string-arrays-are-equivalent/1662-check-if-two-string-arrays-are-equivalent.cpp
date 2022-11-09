class Solution {
public:
    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
      string ans1="";
        string ans2="";
        for(auto x: word1){
            ans1+=x;
        }
        for(auto x: word2){
            ans2+=x;
        }
        return ans1==ans2;
    }
};