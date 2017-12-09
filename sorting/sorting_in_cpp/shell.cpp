#include <iostream>

using namespace std;
void swap(int &a,int &b){
	a^=b^=a^=b;
}
void shellsort(int *ptr,int len){
	
	int span = len/2;
	while(span>=1){
		for(int i=0;i<(len-span);i++)
	    	if(ptr[i]>ptr[i+span])
	        	swap(ptr[i],ptr[i+span]);
	    span=span/2;
	}
	//insertion sort
	int v,j;
	for(int i=1;i<len;i++){
		v=ptr[i];
		j=i;
		while(ptr[j-1]>v){
			ptr[j]=ptr[j-1];
			j--;
		}
		ptr[j]=v;
	}

}
void print(int *ptr,int len){
	for(int i=0;i<len;i++)
		cout << ptr[i] << " ";
	cout<<endl;
}
int main(){
	
	int array[] = {3,66,6,7,22,53,9,61,24,4,2,5};
	int len = sizeof(array)/sizeof(array[0]);
	cout << len << endl;
	
	print(array,len);
	shellsort(array,len);
	print(array,len);
}
