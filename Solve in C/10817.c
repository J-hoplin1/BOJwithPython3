#include<stdio.h>

int main()
{
	int q,w,e,max, count;
	int arr[3];
	scanf("%d %d %d", &arr[0],&arr[1],&arr[2]);
	if(arr[0] >= arr[1])
	{
		max = arr[0];
		arr[0] = arr[1];
		arr[1] = max;
		
	}
	if(arr[1] >= arr[2])
	{
		max = arr[2];
		arr[1] = arr[2];
		arr[2] = max;
	}
	printf("%d",arr[1]);
	
	return 0;
}
