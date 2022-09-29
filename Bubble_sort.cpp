/*Consider the following version of Bubble Sort: 
     for (int i = 0; i < n; i++) {        
            for (int j = 0; j < n - 1; j++)
             {         // Swap adjacent elements if they are in decreasing order      
                    if (a[j] > a[j + 1]) {             swap(a[j], a[j + 1]);     
     }     
     }      
     } 
     Given an array of integers, sort the array in ascending order using the 
     Bubble Sort algorithm above. Once sorted, print the following three lines:  
     Array is sorted in numSwaps swaps., where  is the number of swaps that 
     took place. First Element: firstElement, where  is the first element in the
     sorted array. Last Element: lastElement, where  is the last element in the
     sorted array. Hint: To complete this challenge, you must add a variable that
     keeps a running tally of all swaps that occur during execution.  Example  
     swap    a        0       [6,4,1] 1       [4,6,1] 2       [4,1,6] 3       [1,4,6]
     The steps of the bubble sort are shown above. It took  swaps to sort the array. 
     Output is:  Array is sorted in 3 swaps.   First Element: 1   Last Element: 6   
     Function Description  Complete the function countSwaps in the editor below.  
     countSwaps has the following parameter(s):  int a[n]: an array of integers to 
     sort Prints  Print the three lines required, then return. No return value is expected. 
     Input Format  The first line contains an integer, , the size of the array . The second 
     line contains  space-separated integers .  Constraints  Output Format  
     Sample Input 0  STDIN   Function -----   -------- 3       a[] size n = 3 1 2 3   a = [1, 2, 3] 
     Sample Output 0  Array is sorted in 0 swaps. First Element: 1 Last Element: 3 Explanation 0
     The array is already sorted, so  swaps take place.  Sample Input 1  3 3 2 1 Sample Output 1 
     Array is sorted in 3 swaps. First Element: 1 Last Element: 3 Explanation 1 The array is not 
     sorted, and its initial values are: . The following  swaps take place:  
     At this point the array is sorted and the three lines of output are printed to stdout.*/

#include <iostream>

#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'countSwaps' function below.
 *
 * The function accepts INTEGER_ARRAY a as parameter.
 */
  
void countSwaps(vector<int> a) {
    int counts=0;
    int n=a.size();
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n-1;j++)
        {
            if(a[j]>a[j+1])
            {
                swap(a[j],a[j+1]);
                counts++;
            }
        }
    }
    cout<<"Array is sorted in "<<counts<<" swaps."<<endl;
    cout<<"First Element: "<<a[0]<<endl;
    cout<<"Last Element: "<<a[a.size()-1]<<endl;
}


int main()
{
    string n_temp;
    getline(cin, n_temp);

    int n = stoi(ltrim(rtrim(n_temp)));

    string a_temp_temp;
    getline(cin, a_temp_temp);

    vector<string> a_temp = split(rtrim(a_temp_temp));

    vector<int> a(n);

    for (int i = 0; i < n; i++) {
        int a_item = stoi(a_temp[i]);

        a[i] = a_item;
    }

    countSwaps(a);

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
