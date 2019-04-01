#include <stdio.h>

int main()
{
	int input = 0;
	scanf("%d", &input);
	int count = 1;
	for(;count <= input;count++)
	{
		printf("%d\n", count);
	}
	return 0;
}
