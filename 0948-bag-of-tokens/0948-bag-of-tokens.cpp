class Solution {
public:
    int bagOfTokensScore(vector<int>& tokens, int power) {
        int l=0, r=tokens.size()-1, score=0;
        
        sort(tokens.begin(), tokens.end());
        while(l<=r){
            if(power >= tokens[l]){
                power-=tokens[l++];
                score++;
            }
            else if(power+tokens[r]>=tokens[l] && score!=0 && r!=l){
                power += tokens[r--];
                score--;
            }
            else{
                break;
            }
        }
       return score; 
    }
};