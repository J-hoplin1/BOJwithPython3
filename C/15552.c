#include<stdio.h>
#include<stdlib.h>

typedef struct{
	int a;
	int b;
}node;

typedef struct{
	node *arr;
}total;

int main()
{
	total A;
	int count;
	int index = 0;
	scanf("%d", &count);
	A.arr = calloc(count,sizeof(node));
	for(;index < count;index++)
	{
		scanf("%d %d",&A.arr[index].a,&A.arr[index].b);
	}
	for(index = 0;index < count;index++)
	{
		printf("%d\n", A.arr[index].a + A.arr[index].b);
	}
	free(A.arr);
}
