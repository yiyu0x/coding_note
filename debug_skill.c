#include <stdio.h>
#define LOCAL //debug skill

int main(){

#ifdef LOCAL
	printf("hello\n\n");
#endif

	int n;
	//scanf have return value !! (value is input quantity)
	while(scanf("%d",&n)==1&&n!=0){
		printf("%d\n",n);
	}
}
