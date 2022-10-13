#include <bits/stdc++.h>
using namespace std;
double Theatre(double x,double y,double z)
{
	return ceil(x/z)*ceil(y/z);
}
int main ()
{
	double n,m,a;
	cin>>n>>m>>a;
	cout<<(long long)Theatre(n,m,a);
	return 0;
}
