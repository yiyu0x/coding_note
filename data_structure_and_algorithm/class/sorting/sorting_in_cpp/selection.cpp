#include <iostream>
using namespace std;
void exange(int &a,int &b){
	int t=a;
	a=b;
	b=t;
}
int main(){
	
	int min;
	int a[] = {1,6,3,7,8,3,5,72,8,3,6};
	for(int i=1;i<=sizeof(a)/sizeof(a[0]);i++){
		
		min = i;
		for(int j=i+1;j<=sizeof(a)/sizeof(a[0]);j++){
			if(a[j]<a[min])
				min = j;
		}	
		exange(a[i],a[min]);
	}

	for(int i=1;i<=sizeof(a)/sizeof(a[0]);i++){
		cout << a[i] << " ";
	}
}
