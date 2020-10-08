#include<stdio.h>
#include<stdlib.h>

typedef struct {
	int size;
	int *arr1;
}node;

typedef struct{
	node *arr;
	int *total;
}total;

int main()
{
	total a;
	int input;
	int count = 0;
	int count1 = 0;
	int count_node = 0;
	float average = 0;
	scanf("%d", &input);
	a.arr = calloc(input,sizeof(node));
	a.total = calloc(input,sizeof(int));
	for(count = 0;count < input;count++)
	{
		scanf("%d",&a.arr[count].size);
		a.arr[count].arr1 = calloc(a.arr[count].size,sizeof(int));
		for(count1 = 0;count1 < a.arr[count].size;count1++)
		{
			scanf("%d",&a.arr[count].arr1[count1]);
			a.total[count] += a.arr[count].arr1[count1];
		}
	}
	for(count = 0;count < input;count++)
	{
		count_node = 0;
		average = (float)a.total[count] / (float)a.arr[count].size;
		for(count1 = 0;count1<a.arr[count].size;count1++)
		{
			if(a.arr[count].arr1[count1] > average)
			{
				count_node += 1;
			}
			else
			{
				continue;
			}
		}
		printf("%.3f%%\n",((float)count_node / (float)a.arr[count].size) * 100);
	}
	return 0;
}
