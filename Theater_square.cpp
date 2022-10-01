#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    float n,m,a,l,w;
    cout<<"Enter the length and width of the square and the length of the flagstone"<<endl;
    cin>>n>>m>>a;
    l= ceil(n/a);
    w= ceil(m/a);
    long long result= l*w;
    cout<<result;
    return 0;
}
