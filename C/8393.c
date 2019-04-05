#include<stdio.h>

int main()
{
	int input,sum, result = 0;
	scanf("%d", &input);
	for(sum = 1;sum <=input;sum++)
	{
		result += sum;
	}
	printf("%d", result);
	return 0;
}
