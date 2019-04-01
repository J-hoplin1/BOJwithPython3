#include <stdio.h>

int main()
{
	int input = 0;
	scanf("%d",&input);
	int count1 = 1;
	int count2;
	for(;count1 <= input;count1++)
	{
		for(count2 = 1;count2 <= count1;count2++)
		{
			printf("*");
		}
		printf("\n");
	}
	return 0;
}

