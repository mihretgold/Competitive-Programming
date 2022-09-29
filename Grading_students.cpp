/*HackerLand University has the following grading policy: Every student receives a in the inclusive range from to .
 Any less than is a failing grade. Sam is a professor at the university and likes to round each student's 
 according to these rules: If the difference between the and the next multiple of is less than , round up 
 to the next multiple of . If the value of is less than , no rounding occurs as the result will still be a 
 failing grade. Examples round to (85 - 84 is less than 3) do not round (result is less than 40) do not 
 round (60 - 57 is 3 or higher) Given the initial value of for each of Sam's students, write code to 
 automate the rounding process. Function Description Complete the function grading Students in the editor
  below. grading Students has the following parameter(s): int grades[n]: the grades before rounding Returns 
  int[n]: the grades after rounding as appropriate Input Format The first line contains a single integer, , 
  the number of students. Each line of the subsequent lines contains a single integer, . Constraints 
  Sample Input 0 4 73 67 38 33 Sample Output 0 75 67 40 33 Explanation 0 image Student received a ,
   and the next multiple of from is . Since , the student's grade is rounded to . Student received a ,
    and the next multiple of from is . Since , the grade will not be modified and the student's final grade is .
     Student received a , and the next multiple of from is . Since , 
the student's grade will be rounded to . Student received a grade below , so the grade will not be modified and 
the student's final grade is .*/

#include <iostream>
#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'gradingStudents' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts INTEGER_ARRAY grades as parameter.
 */

vector<int> gradingStudents(vector<int> grades) {
  
      int l= grades.size();
    for(int i=0; i<l; i++){
        if(grades[i]>= 38 & grades[i] <= 100){
            if((grades[i]+ 1) % 5 == 0 )
            grades[i] = grades[i] + 1;
            else if((grades[i]+ 2) % 5 == 0)
            grades[i] = grades[i] + 2;
            else
            grades[i]= grades[i];
        }
    }
    return grades;
}


int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string grades_count_temp;
    getline(cin, grades_count_temp);

    int grades_count = stoi(ltrim(rtrim(grades_count_temp)));

    vector<int> grades(grades_count);

    for (int i = 0; i < grades_count; i++) {
        string grades_item_temp;
        getline(cin, grades_item_temp);

        int grades_item = stoi(ltrim(rtrim(grades_item_temp)));

        grades[i] = grades_item;
    }

    vector<int> result = gradingStudents(grades);

    for (size_t i = 0; i < result.size(); i++) {
        fout << result[i];

        if (i != result.size() - 1) {
            fout << "\n";
        }
    }

    fout << "\n";

    fout.close();

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
