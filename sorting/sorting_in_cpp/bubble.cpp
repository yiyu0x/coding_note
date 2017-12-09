#include <iostream>
using namespace std;


void swap(int &a,int &b){
	a^=b^=a^=b;
}
int main(){

	int a[]= { 5,66,46,2,74,23,75,35,8,3,7,4,2,1};
	int tmp,j;
	bool change;
	int times = sizeof(a)/sizeof(a[0]);
	do{
		change = false;
		for(j=1;j<sizeof(a)/sizeof(a[0]);j++){
			if(a[j-1]>a[j]){
			
				swap(a[j-1],a[j]);
				change = true;
			}
		}	
	}while(change);


	for(j=0;j<sizeof(a)/sizeof(a[0]);j++){
		cout << a[j] << " ";
	}
}
