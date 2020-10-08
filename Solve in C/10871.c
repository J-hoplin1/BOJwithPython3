#include<stdio.h>
#include<stdlib.h>

int main()
{
	int total, standard, count;
	int *arr;
	scanf("%d %d", &total, &standard);
	arr = calloc(total,sizeof(int));
	for(count = 0;count < total;count++)
	{
		scanf("%d",&arr[count]);
	}
	for(count = 0; count<total;count++)
	{
		if(arr[count] < standard)
		{
			printf("%d", arr[count]);
		}
		else
		{
			continue;
		}
		printf(" ");
	}
	return 0;
}
