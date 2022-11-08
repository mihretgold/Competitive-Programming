class Solution {
public:
    string removeDigit(string number, char digit) {
        int n=number.size();
        for(int i=0; i<n; i++){
            if(number[i]==digit && number[i] < number[i+1]){//if we find the digit and the num < next num
                number.erase(i,1);
                return number;
            }
        }
        int last=number.find_last_of(digit);//otherwise remove the last occurance of the number
        number.erase(last,1);       
        return number;
    }
};
