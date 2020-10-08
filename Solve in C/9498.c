#include<stdio.h>

int main()
{
	int input;
	scanf("%d", &input);
	if(input >=90 && input <= 100)
	{
		printf("A\n");
		return 0;
	}
	else if(input >= 80 && input <= 89)
	{
		printf("B\n");
		return 0;
	}
	else if (input >= 60 && input <= 69)
	{
		printf("D\n");
		return 0;
	}
	else
	{
		printf("F\n");
		return 0;
	}
}
