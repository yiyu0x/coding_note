#include <iostream>
using namespace std;

int main(){
	int v,j;
	int a[] = {2,6,8,3,5,8,3,4};
	for(int i=2;i<=sizeof(a)/sizeof(a[0]);i++){
		v=a[i];
		j=i;
		while(a[j-1]>v){
			a[j]=a[j-1];
			j--;
		}
		a[j]=v;
	}

	for(int i=0;i<sizeof(a)/sizeof(a[0]);i++){
		cout << a[i] << " ";
	}
}
