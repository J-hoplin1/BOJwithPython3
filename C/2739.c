#include <stdio.h>

int main()
{
	int input = 0;
	int count = 1;
	scanf("%d", &input);
	for(;count <= 9; count ++)
	{
		printf("%d * %d = %d\n",input,count,input*count);
	}
	return 0;
}
