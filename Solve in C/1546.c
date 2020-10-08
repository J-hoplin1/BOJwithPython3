#include<stdio.h>
#include<stdlib.h>

int main()
{
	int total,count,max = 0,input,ck_index;
	float total_a = 0;
	scanf("%d", &total);
	float *arr = calloc(total,sizeof(float));
	for(count = 0;count < total;count++)
	{
		scanf("%d", &input);
		arr[count] = input;
		if(input > max)
		{
			max = input;
		}
	}
	for(count = 0;count < total;count++)
	{
		arr[count] = (arr[count] / max) * 100;
		total_a += arr[count];
	}
	printf("%.2f",total_a / total);
	return 0;
}
