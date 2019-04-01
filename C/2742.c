#include <stdio.h>

int main()
{
	int input = 0;
	scanf("%d", &input);
	int count = 1;
	for(;count <= input;input--)
	{
		printf("%d\n", input);
	}
	return 0;
}
