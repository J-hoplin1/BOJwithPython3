#include<stdio.h>

int main()
{
	int input = 0;
	scanf("%d", &input);
	int count1 = 1;
	int count2;
	int count3;
	for(;count1 <= input; count1++)
	{
		
		for(count2 = input - count1;count2 >= 1;count2--)
		{
			printf(" ");
		}
		count2 = input - count1;
		for(count3 = input - count2;count3>=1;count3--)
		{
			printf("*");
		}
		printf("\n");
	}
	return 0;
}
