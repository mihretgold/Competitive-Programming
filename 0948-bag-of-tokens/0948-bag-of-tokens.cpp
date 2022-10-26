class Solution {
public:
    /*
    
    [100,200,300,400], power =500 s=0
    
    //is it sorted
    -sort
    -if v[0]>p return 0
    -else v[i]-p s++
    s!=0 V[n-1]+p s--
    [100,200], power = 50 s=1
     
    */
   int bagOfTokensScore(vector<int>& tokens, int power) {
        int n=tokens.size();
        int s=0, e=n-1, score=0;
        
        sort(tokens.begin(), tokens.end());//sort tokens
        while(s<=e){
            if(power >= tokens[s]){//if there is enough power for tokens to subtract from
                power-=tokens[s++];
                score++;
            }
            else if(power+tokens[e]>=tokens[s] && score!=0 && e!=s){//if adding the tokens[e] element will get the score back or is >= tokens[s] element
                power += tokens[e--];
                score--;
            }
            else{//if it wont get the score back we break
                break;
            }
        }
       return score; 
    }
};