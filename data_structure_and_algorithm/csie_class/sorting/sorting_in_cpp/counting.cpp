// code from : https://www.byvoid.com/zht/blog/sort-radix
// liner sorting introduction
#include <iostream>
#include <cmath>
using namespace std;
void CountingSort(int *A,int *B,int *Order,int N,int K)
{
    int *C=new int[K+1];
    int i;
    memset(C,0,sizeof(int)*(K+1));
    for (i=1;i<=N;i++) //把A中的每個元素分配
        C[A[i]]++;
    for (i=2;i<=K;i++) //統計不大於i的元素的個數
        C[i]+=C[i-1];
    for (i=N;i>=1;i--)
    {
        B[C[A[i]]]=A[i]; //按照統計的位置，將值輸出到B中，將順序輸出到Order中
        Order[C[A[i]]]=i;
        C[A[i]]--;
    }
}
int main()
{
    int *A,*B,*Order,N=15,K=10,i;
    A=new int[N+1];
    B=new int[N+1];
    Order=new int[N+1];
    for (i=1;i<=N;i++)
        A[i]=rand()%K+1; //生成1..K的隨機數
    printf("Before CS:\n");
    for (i=1;i<=N;i++)
        cout << A[i] << " ";
    CountingSort(A,B,Order,N,K);
    cout << "\nAfter CS:\n";
    for (i=1;i<=N;i++)
        cout << B[i] << " ";
    cout << "\nOrder:\n";
    for (i=1;i<=N;i++)
        cout << Order[i] << " ";
    return 0;
}
