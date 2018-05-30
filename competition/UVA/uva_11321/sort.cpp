#include <iostream>
#include <algorithm>
//uva 11321
using namespace std;
int mod;
bool CMP(int x,int y){
	// if mod value are different , small first.	
	if(x%mod != y%mod) return x%mod < y%mod;
	// if two value are not same odd or even , odd first.
	if(abs(x%2) != abs(y%2)) return abs(x%2);
	// if two value are odd , big first.
	if(abs(x%2)) return x>y;
	// if two valure are even , small first.
	return x<y;
}
int main(){
	int n;	
	while(cin>>n>>mod && n && mod){
		int data[n];
		for(int i=0;i<n;i++) cin >> data[i];
		sort(data,data+n,CMP);
		for(int i=0;i<n;i++) cout << data[i] << endl;
	}
}
