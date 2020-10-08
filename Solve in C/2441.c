#include<stdio.h>

int main()
{
	int input,count,count2;
	scanf("%d", &input);
	int input_n = input;
	for(;input_n > 0;input_n--)
	{
		for(count2 = 0;count2 < input - input_n; count2 ++)
		{
			printf(" ");
		}
		for(count = 1;count <= input_n;count++)
		{
			printf("*");
		}
		printf("\n");
	}
	return 0;
}
