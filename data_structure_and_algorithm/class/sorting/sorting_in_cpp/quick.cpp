#include <iostream>
using namespace std;
int len;
void printArray(int *arr){
	for(int i=0;i<len;i++){
		cout << arr[i] << " ";
	}
	printf("\n");
}
void swap(int *a,int *b){
	int tmp =*a;
	*a=*b;
	*b=tmp;
}
int qs(int *arr,int left,int right){
	if(left >= right)
		return 0;
	int pivot_item = arr[left];
	int j=left;

	for(int i=left+1;i<=right;i++){
		if(arr[i]>=pivot_item)
			continue;
		j++;
		swap(&arr[i],&arr[j]);	
	}
	int pivot_point = j;
	swap(&arr[left],&arr[pivot_point]);

	// this switch is print porcess
	// printArray(arr);
	qs(arr,left,pivot_point-1);
	qs(arr,pivot_point+1,right);
	return 1;
}

int main(){
	int array[] = {0,9,7,9,35,1,0,8,1,6,33,22,11,13,13};
	len = sizeof(array)/sizeof(array[0]);
	
	qs(array,0,len-1);
	printArray(array);
}
